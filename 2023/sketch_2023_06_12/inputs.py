def get_arduino(port=None):
    """
    This is a PyFirmata 'helper' that tries to connect to an Arduino
    compatible board.
    
    If no port is informed, using pyserial's serial.tools.list_ports.comports(),
    if one port is found, tries that one. If more than one port is found,
    shows for the user to choose one. Returns None if no port is found or if the
    user cancels the dialog.
    
    If it successfully connects, it will return a pyfirmata Arduino object,
    but before that, it starts a pyfirmata.util.Iterator, and adds to the object
    both analog_read() and digital_read() functions that mimic Processing's
    Firmata library interface:
    Readings are never None, and analog pins return a value between 0 and 1023.
    """   
    from pyfirmata import Arduino, util
    from serial.tools import list_ports
    
    comports = [comport.device for comport in list_ports.comports()]
    if not comports:
        print('No ports found.')
        return None
    elif isinstance(port, str) and port not in comports:
        print(f'Port "{port}" not found.')
        return None
    elif isinstance(port, int):
        if port >= len(comports):
            print(f'Port [{port}] not found.')
            return None
        else:
            port = comports[port]
    elif len(comports) == 1:
        port = comports[0]
    elif port is None:
        port = option_pane(
            'Where is your board?',
            'Please select the USB port where your '
            'Arduino compatible board is connected:',
            comports,
            -1)  # index for default option
        if port is None:
            print('No port selected.')
            return None
    try:
        print(f'Connecting to port {port}...')
        arduino = Arduino(port)
        util.Iterator(arduino).start()
    except Exception as e:
        print(repr(e))
        return None
    # Prepare analog_read() for A0 A1 A2 A3 A4 A5
    for a in range(6):  
        arduino.analog[a].enable_reporting()
    arduino.analog_read = (lambda a: round(arduino.analog[a].read() * 1023)
                           if arduino.analog[a].read() is not None
                           else 0)
    # Prepare digital_read() for D2 to D13
    digital_pin_dict = {d: arduino.get_pin(f'd:{d}:i')
                        for d in range(2, 14)}
    for d in digital_pin_dict.keys():
        digital_pin_dict[d].enable_reporting()
    arduino.digital_read = (lambda d: digital_pin_dict[d].read()
                            if digital_pin_dict[d].read() is not None
                            else False)
    return arduino


def option_pane(title, message, options, default=None, index_only=False):
    """
    A helper for Java swing JOptionPane input dialog with drop down options.
    
    title     : str   - Dialog window's title (make it shorter than message).
    message   : str   - Text shown before the drop down.
    options   : list  - List of strings to show in the drop down.
    default   : int   - None or index to the pre-selected option in the list.
    index_only: False - Function returns an option string from the options list
                        provided, or None, if the dialog was cancelled;
                True  - Function returns the position index to the options list.    
    """
    from javax.swing import JOptionPane
    
    if default is None:
        default = options[0]
    elif index_only:
        default = options[default]

    selection = JOptionPane.showInputDialog(
        None,     # frame
        message,
        title,
        JOptionPane.INFORMATION_MESSAGE,
        None,     # for Java null
        options,
        default)  # must be in options, otherwise first is shown
    if selection:
        if index_only:
            return options.index(selection)
        else:
            # Trouble: selection can be java.lang.String
            return str(selection) if selection else None
