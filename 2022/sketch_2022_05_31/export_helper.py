def save_png_with_src(output, *args, **kwargs):
    import PIL
    import py5
    import __main__ as m

    with open(m.__file__) as f:
        src = ''.join(f.read())

    metadata = PIL.PngImagePlugin.PngInfo()

    context = kwargs.pop('context', None)
    if context:
        metadata.add_itxt("context", context)   
    metadata.add_itxt("code", src)
    py5.save(output, *args, pnginfo=metadata, **kwargs)
    # read back and print...
    # target_image = PIL.Image.open(output)
    # print(target_image.info['code'])