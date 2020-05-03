linhas = ["tecle 'o' para abrir um arquivo",
          "tecle 'a' para apagar a lista"]

def setup():
    size(400, 400)

def draw():
    background(0)
    fill(100, 100, 255)
    textAlign(LEFT, TOP)
    textSize(20)
    for i, linha in enumerate(linhas):
        x = 10 + 120 * (i // 20)
        y = i * 19 - 380 * (i // 20)            
        text(linha, x, y) 
        
def keyPressed():
    if key == 'o':
        selectInput("escolha um arquivo:", "file_selected")
    if key == 'a':
        linhas[:] = []
    if key == 's':
        saveFrame("select_input.png")
        
def file_selected(selection):
    if selection == None:
        print(u"Seleção cancelada.")
    else:
        path = selection.getAbsolutePath()
        print("Arquivo selecionado: " + path)
        linhas.extend(loadStrings(path)) 
        
                        
        
    
    
    
