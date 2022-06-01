def save_png_with_src(output=None, *args, **kwargs):
    import PIL
    import py5
    from datetime import datetime
    import __main__ as m
    
    src_file = m.__file__
    
    if output is None:
        ts = str(datetime.now())[:19]
        output = ts.replace(' ', '_').replace(':', '-') + '.png'
    
    with open(src_file) as f:
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