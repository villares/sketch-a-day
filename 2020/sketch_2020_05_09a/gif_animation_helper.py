"""
Alexandre B A Villares http://abav.lugaralgum.com - GPL v3 

A helper for the Processing gifAnimation library https://github.com/extrapixel/gif-animation/tree/3.0
Download from https://github.com/villares/processing-play/blob/master/export_GIF/unzip_and_move_to_libraries_GifAnimation.zip
This helper was inspired by an example by Art Simon https://github.com/APCSPrinciples/AnimatedGIF/

v2019_09_23

# add at the start of your sketch:
  add_library('gifAnimation')
  from gif_animation_helper import gif_export
# add at the end of draw():
  gif_export(GifMaker, "filename")
"""

def gif_export(GifMaker,             # gets a reference to the library
               filename="exported",  # .gif will be added
               repeat=0,             # 0 makes it an "endless" animation
               quality=32,          # quality range 0 - 255
               delay=200,            # this is quick
               frames=0,             # 0 will stop on keyPressed or frameCount >= 100000
               finish=False):        # force stop
    global gifExporter
    try:
        gifExporter
    except NameError:
        gifExporter = GifMaker(this, filename + ".gif")
        gifExporter.setRepeat(repeat)
        gifExporter.setQuality(quality)
        gifExporter.setDelay(delay)
        print("gif recording started")


    gifExporter.addFrame()

    if (frames == 0 and keyPressed and key == "e" or
        frames != 0 and frameCount >= frames):
        finish = True
                
    if finish:
        gifExporter.finish()
        print("gif saved, exit")
        exit()
