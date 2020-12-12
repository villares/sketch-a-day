""" 
More naive graph drawing 
"""

nodes = []
edges = []
NODE_SIZE = 50  # Diâmetro dos nodes
EDGE_SIZE = 100  # Distância sugerida para Edges
BACKGROUND = color(10, 0, 0)

def setup():
    size(400, 400)
    strokeWeight(3)
    # graph = read_csv("graph.txt")
    # Dictionary (hash map) of nodes and a list of connections (to make edges)

    graph = {'A': ['B'], 'B': ['C'], 'C': ['A', 'B'],
             'D': ['A'], 'E': ['A'], 'F': ['B'], 'G': ['F'],
             'Z': ['W'], 'W': ['X', 'Y'], 'Y': ['W'], 'X': []
             }
    # create Node objects for each dictionary item
    for name in graph:
        x = random(width * .25, width * .75)
        y = random(height * .25, height * .75)
        new_node = Node(x, y, name)
        nodes.append(new_node)

    for name in graph:
        n1 = Node.from_name(name)  # find the Node object from its "name"
        for other in graph[name]:
            n2 = Node.from_name(other)  # for each connection, find Node obj
            # n2 not none and n1, n2 Edge not yet made          
            if n2 and not Edge.find(n1, n2):
                new_edge = Edge(n1, n2)    # create an Edge object
                edges.append(new_edge)

def draw():
    background(BACKGROUND)        # limpa a tela
    # para cada Edge
    for e in edges:
        e.plot()  # desenha a linha
        e.ajust(EDGE_SIZE)
    # para cada n
    for n in nodes:
        n.plot()  # desenha
        n.move()  # atualiza posição

# Sob clique do mouse seleciona/deseleciona nodes ou Edgesho
def mouseClicked():
    for n in nodes:   # para cada n checa distância do mouse
        if dist(mouseX, mouseY, n.x, n.y) < NODE_SIZE / 2:
            n.sel = not n.sel  # inverte status de seleção

def keyPressed():   # Quando uma tecla é pressionada
    if key == 'r':  # Se a tecla 'r' for pressionada
        for n in nodes:
            # sorteia nova posição
            x = random(width * .25, width * .75)
            y = random(height * .25, height * .75)
            n.x, n.y = x, y

def mouseDragged():        # quando o mouse é arrastado
    for n in nodes:   # para cada n checa distância do mouse
        if dist(mouseX, mouseY, n.x, n.y) < NODE_SIZE / 2:
            n.x, n.y = mouseX, mouseY
            n.v = PVector(0, 0)

def read_csv(file_name):
    import csv
    # ATENTION! Processing csv reader roots to sketch/data/ folder
    # Pyhton csv module roots to the sketch folder!
    with open(file_name) as f:
        graph = {}
        for record in csv.reader(f):
            cols = [uniname(item.strip(), 'utf-8') for item in record]
            graph[cols[0]] = list(cols[1:])
    return graph


class Node(PVector):

    """
    Node object inherits from PVector so we can do subtraction and 
    find direction between two nodes.
    """

    V_MAX = 2  # velocnameade máxima nas ortogonais vx e vy
    V_MIN = .7

    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y
        self.v = PVector(0, 0)
        self.sel = False   # se está selecionado, começa sem seleção
        self.cor = color(random(128, 255),  # R
                         random(128, 255),  # G
                         random(128, 255),  # B
                         255)              # Alpha ~50%

    def plot(self):
        stroke(self.cor)
        fill(BACKGROUND)
        ellipse(self.x, self.y, NODE_SIZE, NODE_SIZE)
        texto = self.name
        if dist(mouseX, mouseY, self.x, self.y) < NODE_SIZE / 2:
            stroke(255)
            noFill()
            ellipse(self.x, self.y, NODE_SIZE - 5, NODE_SIZE - 5)
        elif self.sel:
            stroke(0)
            noFill()
            ellipse(self.x, self.y, NODE_SIZE - 5, NODE_SIZE - 5)

        fill(self.cor)
        textAlign(CENTER, CENTER)
        text(texto, self.x, self.y)

    def move(self):

        if self.x < NODE_SIZE:
            self.x = NODE_SIZE
        elif self.x > width - NODE_SIZE:
            self.x = width - NODE_SIZE
        if self.y < NODE_SIZE:
            self.y = NODE_SIZE
        elif self.y > height - NODE_SIZE:
            self.y = height - NODE_SIZE

        for n in nodes:
            if n is not self:
                self.ajust(n)

        self.limit_v()
        if not self.sel:
            self.x += self.v.x
            self.y += self.v.y

    def ajust(self, other):
        dir = PVector.sub(self, other)     
        d = dir.mag()
        delta = EDGE_SIZE * 0.9 - d
        if delta > 0:
            dir.mult(delta / 1000)
            self.v += dir
            
    def limit_v(self):
        """ limita à velocidade máxima e para se estiver devagar"""
        if self.v.mag() < Node.V_MIN:
            self.v = PVector(0, 0)
        else:
            self.v.limit(Node.V_MAX)

    @staticmethod
    def from_name(name):
        for p in nodes:
            if p.name == name:
                return p
        return None

class Edge():

    """ Edges have two nodes"""

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.nodes = set((n1, n2))

    def plot(self):
        stroke(255)
        line(self.n1.x, self.n1.y, self.n2.x, self.n2.y)

    def ajust(self, edge_size):
        n1, n2 = self.n1, self.n2
        d = dist(n1.x, n1.y, n2.x, n2.y)
        delta = edge_size - d
        dir = PVector.sub(n1, n2)
        dir.mult(delta / 1000)
        n1.v += dir
        n2.v -= dir

    @staticmethod
    def find(n1, n2):
        """ Is there an Edge with theses Nodes? """
        for e in edges:
            if n1 in e.nodes and n2 in e.nodes:
                return True
        return False
