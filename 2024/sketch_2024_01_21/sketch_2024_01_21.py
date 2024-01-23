import py5

from libretranslatepy import LibreTranslateAPI

url = "https://libretranslate.eownerdead.dedyn.io"
lt = LibreTranslateAPI(url)

def setup():
    py5.size(800, 400)
    py5.background(0)
    py5.color_mode(py5.HSB)

    f = py5.create_font('Inconsolata Black', 80)
    py5.text_font(f)
    py5.text_align(py5.CENTER, py5.CENTER)
    
    t = lt.translate('21 de janeiro de 2024', 'pt', 'en')
    py5.text(t, 400, 200)
    
py5.run_sketch()