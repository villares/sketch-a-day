"""
telemetrix_helper.py
---

An interface for setting up serial comms with a microcontroler board
(usually an Arduino) adding helper methods to a telemetrix board object.

This provides methods to set up and read analog and digital pins,
and also to manage rotary encoders (on digital pins).
"""

import time
import datetime
from serial.tools import list_ports

from telemetrix import telemetrix

def init_board(port=None,
               analog_pins=(),
               digital_pins=(),
               digital_pullup_pins=(),
               analog_differential=5,
               analog_scan_interval=255,
               ):
    """
    Connects to a board running Telemetrix4Arduino and returns a board object
    extended with:
        board.analog_read(pin)                        -> int  0-1023
        board.digital_read(pin)                       -> bool
        board.init_encoder(pin_a, pin_b, pin_sw=None) -> RotaryEncoder

    port                 : None | str | int
        None -> let Telemetrix auto-detect
        str  -> port by name, i.e. 'COM3' or '/dev/ttyUSB0'
        int  -> prot by index from list_ports.comports()
    analog_pins          : iterable of ints
        A-pins to set up analog input mode, read state with analog_read().
    digital_pins         : iterable of ints
        D-pins to set up for digital input, read state with digital_read().
        Do not include any encoder pins or digital_pullup_pins!
    digital_pullup_pins  : iterable of ints
        D-pins to set up for pullup digital input, read state with digital_read().
        Do not include any encoder pins or digital_pins!
    digital_output_pins
    
    analog_differential  : int
        Minimum change before a new reading is reported,
        Lower = more responsive but more serial traffic.
        0 = report every 1-bit change; avoid with multiple analog pins.
    analog_scan_interval  : int
        ms 0-255 (default 255)

    Returns the extended Telemetrix instance, or None on failure.
    """
    com_port = None

    if isinstance(port, str):
        com_port = port
    elif isinstance(port, int):
        comports = [p.device for p in list_ports.comports()]
        if not comports:
            print('No serial ports found.')
            return None
        if port < len(comports):
            com_port = comports[port]

    try:
        if com_port:
            print(f'Connecting to {com_port}...')
            board = telemetrix.Telemetrix(com_port=com_port)
        else:
            print('Connecting (auto-detect)...')
            board = telemetrix.Telemetrix()
    except Exception as exc:
        print(f'Connection failed: {exc!r}')
        return None

    board.set_analog_scan_interval(analog_scan_interval)
    _analog  = {a: 0     for a in analog_pins}
    board._analog = _analog
    _digital = {d: False for d in tuple(digital_pins) + tuple(digital_pullup_pins)}
    board._digital = _digital

    def _make_analog_cb(pin_index):
        def _cb(data):
            _analog[pin_index] = int(data[2])
        return _cb

    def _make_digital_cb(pin_number):
        def _cb(data):
            _digital[pin_number] = bool(data[2])
        return _cb

    for a in analog_pins:
        try:
            board.set_pin_mode_analog_input(a, analog_differential, _make_analog_cb(a))
        except Exception as exc:
            print(f'Warning: could not configure A{a}: {exc!r}')

    for d in digital_pins:
        try:
            board.set_pin_mode_digital_input(d, _make_digital_cb(d))  # pullup: no floating
        except Exception as exc:
            print(f'Warning: could not configure D{d}: {exc!r}')

    for d in digital_pullup_pins:
        try:
            board.set_pin_mode_digital_input_pullup(d, _make_digital_cb(d))  # pullup: no floating
        except Exception as exc:
            print(f'Warning: could not configure pullup D{d}: {exc!r}')

    board.analog_read  = lambda a: _analog.get(a, 0)
    board.digital_read = lambda d: _digital.get(d, False)

    def _encoder(pin_a, pin_b, pin_sw=None):
        return RotaryEncoder(board, pin_a, pin_b, pin_sw)

    board.init_encoder = _encoder

    print(f'Board ready on {com_port or "auto-detected port"}.')
    return board


class RotaryEncoder:
    """
    Rotary encoder to be attached to a Telemetrix board object.
        RotaryEncoder(board, pin_a=pin_a, pin_b=pin_b, pin_sw=pin_sw)
    
    board   : Telemetrix instance returned by init_board()
    pin_a   : int  CLK / A pin number
    pin_b   : int  DT  / B pin number
    pin_sw  : int  push-button pin (active-low, uses internal pull-up)
    
    Usage
    -----
    # At setup
    enc = board.init_encoder(pin_a, pin_b, pin_sw)
    # In loop
    print(enc.position)           # cumulative step count
    print(enc.direction)          # 1 = CW, -1 = CCW, 0 = no recent move
    if enc.consume_press():       # True once per click
        print('button clicked')
    enc.reset()                   # zero the position counter
    """

    DEBOUNCE_S = 0.20   # seconds - minimum time between valid button presses

    
    def __init__(self, board, pin_a, pin_b, pin_sw=None):
        self._pin_a  = pin_a
        self._pin_b  = pin_b
        self._pin_sw = pin_sw

        self._position  = 0
        self._direction = 0
        self._last_a    = 1   # pull-up idles HIGH
        self._last_b    = 1
        # detent-to-detent rotation passes through (0,0) both pins LOW at the
        # midpoint of the cycle. Contact bounce that snaps back to (1,1) early
        # without having visited (0,0) will not be counted.
        self._seen_midpoint  = False
        self._pressed         = False
        self._last_press_time = 0.0
        # Signal pins use pull-up (same as SW) 
        board.set_pin_mode_digital_input_pullup(pin_a, self._encoder_callback)
        board.set_pin_mode_digital_input_pullup(pin_b, self._encoder_callback)
        if pin_sw is not None:
            board.set_pin_mode_digital_input_pullup(pin_sw, self._sw_callback)

    def _encoder_callback(self, data):
        QUAD = {
            (1, 0, 1, 1): +1,   # CW  & returns to rest
            (0, 1, 1, 1): -1,   # CCW & returns to rest
        }        
        pin   = data[1]
        state = data[2]
        # Build the current (a, b) pair, substituting only the pin that fired
        curr_a = state if pin == self._pin_a else self._last_a
        curr_b = state if pin == self._pin_b else self._last_b

        if curr_a == 0 and curr_b == 0:
            self._seen_midpoint = True
        elif curr_a == 1 and curr_b == 1:
            # Returned to rest state - count only if we've been through (0,0)
            if self._seen_midpoint:
                if delta := QUAD.get((self._last_a, self._last_b, 1, 1), 0):
                    self._position  += delta
                    self._direction  = delta
            self._seen_midpoint = False   # reset regardless, bounce or real
        self._last_a = curr_a
        self._last_b = curr_b

    def _sw_callback(self, data):
        if data[2] == 0:  # active-low: 0 means pressed
            now = time.time()
            if now - self._last_press_time >= self.DEBOUNCE_S:
                self._pressed         = True
                self._last_press_time = now

    @property
    def position(self):
        """Cumulative step count (positive = CW, negative = CCW)."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position counter to an arbitrary value."""
        self._position = int(value)

    @property
    def direction(self):
        """Last rotation direction: 1 = CW, -1 = CCW, 0 = not yet moved."""
        return self._direction

    def reset(self):
        """Zero the position counter and clear direction."""
        self._position  = 0
        self._direction = 0

    def consume_press(self):
        """
        Returns True once for each physical button press, then False until
        the button is pressed again.  Safe to poll repeatedly in a loop.
        """
        if self._pressed:
            self._pressed = False
            return True
        return False


if __name__ == '__main__':
    # If CW and CCW are swapped, either flip the +1/-1 signs or swap pin_a/pin_b
    board = init_board(
        #digital_pullup_pins=[2, 3, 4],
        # digital_pins=[...], # also works
        # analog_pins=[0, 1, 2, 3]  # more than 4 analog pins seem to break this!
        ) 
    if board is None:
        print('Could not connect to board.')
        exit()
    print('Ctrl-C for a clean shutdown.')

    enc_a = board.init_encoder(pin_a=13, pin_b=12, pin_sw=11)
    enc_b = board.init_encoder(pin_a=7, pin_b=6, pin_sw=5)
    try:
        while True: 
            if enc_a.consume_press():
                print('[button A pressed]')                
                enc_a.reset()
            if enc_b.consume_press():
                print('[button B pressed]')                
                enc_b.reset()
            print(enc_a.position, enc_a.direction, enc_b.position, enc_b.direction)
            print(board._analog)
            time.sleep(0.05)
    except KeyboardInterrupt:
        print('\nShutting down.')
        board.shutdown()
