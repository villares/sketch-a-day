from inputs import InputInterface

speed = 2
noise_scale = 0.01

def setup():
    global things, w, h, wo, inputs
    size(1200, 800)
    #full_screen()
    color_mode(HSB)
    rect_mode(CENTER)
    no_stroke()
    make_ramp()
    
    inputs = InputInterface()
    
    wo = width / 12
    N = int(wo)
    w = width / N
    h = height / N
    # random bright spots
    things = []
    for i in range(N):
        for j in range(N):
            things.append([w / 2 + i * w,
                           h / 2 + j * h,
                            random(60, 255)])

def draw():
    background(0)
    speed = inputs.analog_read(1) / 100  
    brilho = int(inputs.analog_read(2) / 4) / 255
    modo = int(inputs.analog_read(3))   # modos (x, y),  (x, x) ou (y, x)
    scale_factor = remap(inputs.analog_read(4), 0, 1023, 0.5, 2)
    for x, y, r in things:
        s = noise_scale * scale_factor
        xya = lerp(y, x, ramp[modo])
        xyb = lerp(y, x, ramp[1023 - modo])
        nw = noise(x * s, y * s, xya + 100 + frame_count * speed * s)
        nh = noise(x * s, y * s, xyb + frame_count * speed * 2 * s)
        fw = (2 + w) * nw
        fh = (2 + h) * nh
        matiz = (6 * fw * fh) % 256
        fill(matiz , 150, 255 - r * brilho)    
        rect(x + 2* w * (-.5+nw), y + 2 * h * (-.5+nh), fw, fh)
        
    inputs.update(display=False)
    if is_key_pressed:
        print(
          f'speed: {speed:.1f} brilho: {brilho:.1f} \n'
          f'modo: {modo} {xya == x} {xyb == x} \n'
          f'scale_factor: {scale_factor}'
          )
    
def make_ramp():
    global ramp
    ramp = []
    for x in range(1024):
        if x < 256:
            ramp.append(0)
        elif 256 <= x < 384:
            ramp.append((x - 256) / 128)
        else:
            ramp.append(1)
    
def key_pressed():
    inputs.key_pressed()
    
def key_released():
    inputs.key_released()

