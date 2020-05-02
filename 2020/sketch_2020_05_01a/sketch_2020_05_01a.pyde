
def setup():
    size(400, 400)
    background(0)
    
    linhas = loadStrings("frutas.txt")  # frutas.txt na pasta /data/

    fill(100, 100, 255)
    textAlign(CENTER, CENTER)
    textSize(24)
    for linha in linhas:
        x, y = random(40, 360), random(20, 380)                
        text(linha, x, y)    
        
    saveFrame("read_lines.png")
        
    
    
    
