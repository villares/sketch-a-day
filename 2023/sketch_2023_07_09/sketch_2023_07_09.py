import xml.etree.ElementTree as ET 

import py5

def setup():
    global s
    py5.size(600, 600, py5.P3D)
    vml2obj('building.vml', 'b.obj')
    s = py5.load_shape('b.obj')

def draw():
    py5.background(0)
    py5.lights()
    py5.translate(300, 300)
    py5.scale(10)
    py5.shape(s)

def vml2obj(fin, fout):
    # parse vml file into a tree.
    mytree = ET.parse(fin)   # isso aqui abre e lê o XML
    myroot = mytree.getroot()    
    # prepare to write to file
    with open(fout, 'w') as fobj:
        # lista os vertices preparando a conversão
        iVertex = 0 # contator de vertices
        VertexDicio = dict()
        for vertex in myroot[2][0][0]:
            VertexNum, VertexX, VertexY, VertexZ = vertex.text.split()
            fobj.write('v ' +  str(VertexX) + ' ' +  str(VertexY) + ' ' + str(VertexZ) + '\n')
            iVertex += 1
            VertexDicio[VertexNum] = iVertex
        # lista as faces com os vertices renumerados
        for face in myroot[2][0][1]:
            aface = face.text.split()
            fobj.write('f ')
            for vertice in aface:
                if vertice != '4294967295': # investigar estes casos!
                    fobj.write(str(VertexDicio[vertice]) + ' ')
            fobj.write('\n')
    # Aqui o arquivo fobj vai ser fechado!


py5.run_sketch()
