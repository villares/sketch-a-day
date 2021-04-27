
axioma = "X"
regras = {"X": "F+[[X]-X]-F[-FX]+X",
          "F": "FF"
          }          
tamanho = 5
angulo = 120
iteracoes = 5  # repeticoes (voltas na aplicação das regras)
xo, yo = 300, 500

def setup():
    global frase
    size(600, 600)
    frase = gerar_sistema(iteracoes)
    print(len(frase))

def draw():
    background(240, 240, 200)
    translate(xo, yo)
    desenha_sistema(frase)
    noLoop()
            
def keyPressed():
    global tamanho, angulo, iteracoes, frase
    if key == 'z':
        tamanho -= 1 # tamanho = tamanho - 1
    if key == 'x':
        tamanho += 1
    if key == 'a':
        angulo -= 1
    if key == 's':
        angulo += 1       
    if key == 'q':
        iteracoes -= 1
        frase = gerar_sistema(iteracoes)
        print(len(frase))
    if key == 'w':
        iteracoes += 1   
        frase = gerar_sistema(iteracoes)
        print(len(frase))
    if keyCode == LEFT:  # RIGHT, UP, DOWN
        pass
    redraw()

            
def desenha_sistema(simbolos):
    """
    Recebe uma frase e desenha de acordo com
    as "regras de desenho".
    """
    tamanho_variavel = tamanho
    for simbolo in simbolos:
        if simbolo == "F":
            tamanho_variavel += random(-2, 2)
            line(0, 0, 0, -tamanho_variavel)
            translate(0, -tamanho_variavel)
            fill(255)
            circle(0, 0, tamanho / 3)
        if simbolo == "X":
            fill(0)
            circle(0, 0, tamanho / 3) 
        if simbolo == "+":
            rotate(radians(angulo))
        if simbolo == "-":
            rotate(radians(-angulo))
        if simbolo == "[":
            pushMatrix()
        if simbolo == "]":
            popMatrix()

def gerar_sistema(num):
    """
    Produz a partir da frase na variável global axioma,
    repetindo `num` iterações, um sistema-L seguindo as
    regras do dicionário global `regras`
    """
    frase = axioma
    for i in range(num):
        frase_nova = ""
        for simbolo in frase:
            substituicao = regras.get(simbolo, simbolo)  
            frase_nova = frase_nova + substituicao
        frase = frase_nova
    return frase

# Explicação sobre .get(0 em dicionários
# valor = dicionario.get(chave, valor_caso_nao_encontre_a_chave)
