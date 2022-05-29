import py5

def setup():
    py5.size(600, 600)
    py5.rect(100, 100, 200, 200)
    save_png_with_src('example.png')

def save_png_with_src(output):
    import PIL
    with open(__file__) as f:
        src = ''.join(f.read())
    metadata = PIL.PngImagePlugin.PngInfo()
    metadata.add_itxt("code", src)
    py5.save(output, pnginfo=metadata)
    # read back and print...
    target_image = PIL.Image.open(output)
    print(target_image.info['code'])

py5.run_sketch()
