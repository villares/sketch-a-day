"""
Alexandre B A Villares http://abav.lugaralgum.com - GPL v3 

A helper for the Processing gifAnimation library (https://github.com/jordanorelli)
ported to Processing 3 by 01010101 (https://github.com/01010101)
Download the library from https://github.com/01010101/GifAnimation/archive/master.zip
This helper was inspired by an example by Art Simon https://github.com/APCSPrinciples/AnimatedGIF/

Put  at the start of your sketch:
   add_library('gifAnimation')
   from gif_exporter import gif_export
and at the end of draw():
    gif_export(GifMaker)
"""
def gif_export(GifMaker,             # gets a reference to the library
               filename="exported",  # .gif will be added
               repeat=0,             # 0 makes it an "endless" animation
               quality=32,          # quality range 0 - 255
               delay=170,            # this is quick
               frames=0):            # 0 will stop on keyPressed or frameCount >= 100000
    global gifExporter
    try:
        gifExporter
    except NameError:
        gifExporter = GifMaker(this, filename + ".gif")
        gifExporter.setRepeat(repeat)
        gifExporter.setQuality(quality)
        gifExporter.setDelay(delay)
        
    gifExporter.addFrame()

    if (frames == 0 and keyPressed or frameCount >= 100000) \
            or (frames != 0 and frameCount >= frames):
        gifExporter.finish()
        print("gif saved")
        exit()
