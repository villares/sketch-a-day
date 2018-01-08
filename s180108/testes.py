
def PlatonicFactory(type, c):
  if type == 0:
    s = Tetrahedron(18)
  elif type == 1:
    s = Hexahedron(14)
  elif type == 2:
    s = Octahedron(22)
  elif type == 3:
    s = Dodecahedron(18)
  elif type == 4:
    s = Icosahedron(18)
  s.c = c  # sets a color attribute

  def newCreate(obj):
      fill(obj.c)
      obj.create()
  s.create = newCreate
  return s


class Tetrahedron():
    
  def __init__(radius):
    self.vert = [PVector] * 4
    self.radius = radius
    a = radius * 0.6666
    self.vert[0] = PVector(a, a, a)  # vertex 1
    self.vert[1] = PVector(-a, -a, a)    # vertex 2
    self.vert[2] = PVector(-a, a, -a)  # vertex 3
    self.vert[3] = PVector(a, -a, -a)   # vertex 4
  
  # draws tetrahedron
  def create():
    super.create()
    beginShape(TRIANGLE_STRIP)
    vertex(vert[0].x, vert[0].y, vert[0].z)  # vertex 1
    vertex(vert[1].x, vert[1].y, vert[1].z)    # vertex 2
    vertex(vert[2].x, vert[2].y, vert[2].z)  # vertex 3
    vertex(vert[3].x, vert[3].y, vert[3].z)   # vertex 4
    vertex(vert[0].x, vert[0].y, vert[0].z)  # vertex 1
    vertex(vert[1].x, vert[1].y, vert[1].z)    # vertex 2
    vertex(vert[3].x, vert[3].y, vert[3].z)   # vertex 4
    vertex(vert[2].x, vert[2].y, vert[2].z)  # vertex 3
    vertex(vert[1].x, vert[1].y, vert[1].z)    # vertex 2
    endShape(CLOSE)
  

class Hexahedron extends PlatonicSolid:

  # Tetrahedron
   x, y, z
   radius
   a
  PVector[] vert = PVector[8]
  [][] faces

  # constructor
  Hexahedron( radius) :
    self.radius = radius

    a = radius/1.1414
    faces = [6][4]
    vert[0] = PVector(  a, a, a )
    vert[1] = PVector(  a, a, -a )
    vert[2] = PVector(  a, -a, -a )
    vert[3] = PVector(  a, -a, a )
    vert[4] = PVector( -a, -a, a )
    vert[5] = PVector( -a, a, a )
    vert[6] = PVector( -a, a, -a )
    vert[7] = PVector( -a, -a, -a )

    faces[0] = [] :0, 1, 2, 3
    faces[1] = [] :4, 5, 6, 7
    faces[2] = [] :0, 3, 4, 5
    faces[3] = [] :1, 2, 7, 6
    faces[4] = [] :2, 3, 4, 7
    faces[5] = [] :0, 5, 6, 1
  

  # draws hexahedron 
  def create() : 
    super.create()
    for ( i=0 i<6 i++)
    :
      beginShape()
      for ( j=0 j<4 j++)
      :
        vertex(vert[faces[i][j]].x, vert[faces[i][j]].y, vert[faces[i][j]].z)
      
      endShape()
    
  


class Octahedron extends PlatonicSolid :

  # Octahedron
   x, y, z
   radius

   a
  PVector[] vert = PVector[6]
  [][] faces

  # constructor
  Octahedron( radius) :
    self.radius = radius
    a = radius
    vert[0] = PVector( a, 0, 0 ) 
    vert[1] = PVector( 0, a, 0 )
    vert[2] = PVector( 0, 0, a ) 
    vert[3] = PVector( -a, 0, 0 ) 
    vert[4] = PVector( 0, -a, 0 ) 
    vert[5] = PVector( 0, 0, -a )
  

  # draws octahedron 
  def create() :
    super.create()
    beginShape(TRIANGLE_FAN) 
    vertex(vert[4].x, vert[4].y, vert[4].z)
    vertex(vert[0].x, vert[0].y, vert[0].z)
    vertex(vert[2].x, vert[2].y, vert[2].z)
    vertex(vert[3].x, vert[3].y, vert[3].z)
    vertex(vert[5].x, vert[5].y, vert[5].z)
    vertex(vert[0].x, vert[0].y, vert[0].z)
    endShape()

    beginShape(TRIANGLE_FAN)    
    vertex(vert[1].x, vert[1].y, vert[1].z)
    vertex(vert[0].x, vert[0].y, vert[0].z)
    vertex(vert[2].x, vert[2].y, vert[2].z)
    vertex(vert[3].x, vert[3].y, vert[3].z)
    vertex(vert[5].x, vert[5].y, vert[5].z)
    vertex(vert[0].x, vert[0].y, vert[0].z)
    endShape()
  


class Dodecahedron extends PlatonicSolid :
  # Dodecahedron
   radius
   a, b, c
  PVector[] vert
  [][] faces

  # constructor
  Dodecahedron( radius) :
    self.radius = radius
    a = radius/1.618033989
    b = radius
    c = 0.618033989*a
    faces = [12][5]
    vert = PVector[20]
    vert[ 0] = PVector(a, a, a)
    vert[ 1] = PVector(a, a, -a)
    vert[ 2] = PVector(a, -a, a)
    vert[ 3] = PVector(a, -a, -a)
    vert[ 4] = PVector(-a, a, a)
    vert[ 5] = PVector(-a, a, -a)
    vert[ 6] = PVector(-a, -a, a)
    vert[ 7] = PVector(-a, -a, -a)
    vert[ 8] = PVector(0, c, b)
    vert[ 9] = PVector(0, c, -b)
    vert[10] = PVector(0, -c, b)
    vert[11] = PVector(0, -c, -b)
    vert[12] = PVector(c, b, 0)
    vert[13] = PVector(c, -b, 0)
    vert[14] = PVector(-c, b, 0)
    vert[15] = PVector(-c, -b, 0)
    vert[16] = PVector(b, 0, c)
    vert[17] = PVector(b, 0, -c)
    vert[18] = PVector(-b, 0, c)
    vert[19] = PVector(-b, 0, -c)

    faces[ 0] = [] :0, 16, 2, 10, 8
    faces[ 1] = [] :0, 8, 4, 14, 12
    faces[ 2] = [] :16, 17, 1, 12, 0
    faces[ 3] = [] :1, 9, 11, 3, 17
    faces[ 4] = [] :1, 12, 14, 5, 9
    faces[ 5] = [] :2, 13, 15, 6, 10
    faces[ 6] = [] :13, 3, 17, 16, 2
    faces[ 7] = [] :3, 11, 7, 15, 13
    faces[ 8] = [] :4, 8, 10, 6, 18
    faces[ 9] = [] :14, 5, 19, 18, 4
    faces[10] = [] :5, 19, 7, 11, 9
    faces[11] = [] :15, 7, 19, 18, 6
  

  # draws dodecahedron 
  def create() :
    super.create()
    for ( i=0 i<12 i++)
    :
      beginShape()
      for ( j=0 j<5 j++)
      :
        vertex(vert[faces[i][j]].x, vert[faces[i][j]].y, vert[faces[i][j]].z)
      
      endShape()
    
  
