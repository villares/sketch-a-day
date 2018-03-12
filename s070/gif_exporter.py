def gif_export(GifMaker=None,
               filename="exported",
               repeat=0,
               quality=255,
               delay=170,
               frames=0):
    """
    Be careful! frames=0 will stop the sketch on keyPressed or frameCount >= 100000... 
    """
    if GifMaker:
        global gifExporter
        file = filename + ".gif"
        gifExporter = GifMaker(this, file)
        print("saving to " + file)
        gifExporter.setRepeat(repeat)  # 0 makes it an "endless" animation
        gifExporter.setQuality(255)  # quality range 0 - 255
        gifExporter.setDelay(delay)

    if not frameCount % 10:
        gifExporter.addFrame()

    if (frames == 0 and keyPressed or frameCount >= 100000) \
            or (frames != 0 and frameCount >= frames):
        gifExporter.finish()
        print("gif saved")
        exit()
