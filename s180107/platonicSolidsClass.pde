class PlatonicSolid {
  color c = color(255);
  void create() {
    fill(this.c);
    //implemented by each solid
  }
}

PlatonicSolid PlatonicFactory(int type, color c) {
  PlatonicSolid s = new PlatonicSolid();
  switch(type) {
  case 0:  
    s = new Tetrahedron(18); 
    break;
  case 1:  
    s = new Hexahedron(14);
    break;
  case 2:  
    s = new Octahedron(22);    
    break;
  case 3:  
    s = new Dodecahedron(18);    
    break;
  case 4:  
    s = new Icosahedron(18);    
    break;
  }
  s.c = c; // sets color attribute
  return s;
}
class Icosahedron extends PlatonicSolid {
  // icosahedron
  float radius;
  PVector topPoint;
  PVector[] topPent = new PVector[5];
  PVector bottomPoint;
  PVector[] bottomPent = new PVector[5];
  float angle = 0;
  float triDist;
  float triHt;
  float a, b, c;

  // constructor
  Icosahedron(float radius) {
    this.radius = radius;
    c = dist(cos(0)*radius, sin(0)*radius, cos(radians(72))*radius, sin(radians(72))*radius);
    b = radius;
    a = (float)(Math.sqrt(((c*c)-(b*b))));
    triHt = (float)(Math.sqrt((c*c)-((c/2)*(c/2))));
    for (int i=0; i<topPent.length; i++) {
      topPent[i] = new PVector(cos(angle)*radius, sin(angle)*radius, triHt/2.0f);
      angle+=radians(72);
    }
    topPoint = new PVector(0, 0, triHt/2.0f+a);
    angle = 72.0f/2.0f;
    for (int i=0; i<topPent.length; i++) {
      bottomPent[i] = new PVector(cos(angle)*radius, sin(angle)*radius, -triHt/2.0f);
      angle+=radians(72);
    }
    bottomPoint = new PVector(0, 0, -(triHt/2.0f+a));
  }

  // draws icosahedron 
  void create() {
    super.create();
    for (int i=0; i<topPent.length; i++) {
      // icosahedron top
      beginShape();
      if (i<topPent.length-1) {
        vertex(topPent[i].x, topPent[i].y, topPent[i].z);
        vertex(topPoint.x, topPoint.y, topPoint.z);
        vertex(topPent[i+1].x, topPent[i+1].y, topPent[i+1].z);
      } else {
        vertex(topPent[i].x, topPent[i].y, topPent[i].z);
        vertex(topPoint.x, topPoint.y, topPoint.z);
        vertex(topPent[0].x, topPent[0].y, topPent[0].z);
      }
      endShape(CLOSE);

      // icosahedron bottom
      beginShape();
      if (i<bottomPent.length-1) {
        vertex(bottomPent[i].x, bottomPent[i].y, bottomPent[i].z);
        vertex(bottomPoint.x, bottomPoint.y, bottomPoint.z);
        vertex(bottomPent[i+1].x, bottomPent[i+1].y, bottomPent[i+1].z);
      } else {
        vertex(bottomPent[i].x, bottomPent[i].y, bottomPent[i].z);
        vertex(bottomPoint.x, bottomPoint.y, bottomPoint.z);
        vertex(bottomPent[0].x, bottomPent[0].y, bottomPent[0].z);
      }
      endShape(CLOSE);
    }

    // icosahedron body
    for (int i=0; i<topPent.length; i++) {
      if (i<topPent.length-2) {
        beginShape();
        vertex(topPent[i].x, topPent[i].y, topPent[i].z);
        vertex(bottomPent[i+1].x, bottomPent[i+1].y, bottomPent[i+1].z);
        vertex(bottomPent[i+2].x, bottomPent[i+2].y, bottomPent[i+2].z);
        endShape(CLOSE);

        beginShape();
        vertex(bottomPent[i+2].x, bottomPent[i+2].y, bottomPent[i+2].z);
        vertex(topPent[i].x, topPent[i].y, topPent[i].z);
        vertex(topPent[i+1].x, topPent[i+1].y, topPent[i+1].z);
        endShape(CLOSE);
      } else if (i==topPent.length-2) {
        beginShape();
        vertex(topPent[i].x, topPent[i].y, topPent[i].z);
        vertex(bottomPent[i+1].x, bottomPent[i+1].y, bottomPent[i+1].z);
        vertex(bottomPent[0].x, bottomPent[0].y, bottomPent[0].z);
        endShape(CLOSE);

        beginShape();
        vertex(bottomPent[0].x, bottomPent[0].y, bottomPent[0].z);
        vertex(topPent[i].x, topPent[i].y, topPent[i].z);
        vertex(topPent[i+1].x, topPent[i+1].y, topPent[i+1].z);
        endShape(CLOSE);
      } else if (i==topPent.length-1) {
        beginShape();
        vertex(topPent[i].x, topPent[i].y, topPent[i].z);
        vertex(bottomPent[0].x, bottomPent[0].y, bottomPent[0].z);
        vertex(bottomPent[1].x, bottomPent[1].y, bottomPent[1].z);
        endShape(CLOSE);

        beginShape();
        vertex(bottomPent[1].x, bottomPent[1].y, bottomPent[1].z);
        vertex(topPent[i].x, topPent[i].y, topPent[i].z);
        vertex(topPent[0].x, topPent[0].y, topPent[0].z);
        endShape(CLOSE);
      }
    }
  }
}


class Tetrahedron extends PlatonicSolid {

  // Tetrahedron
  float radius;
  float a;
  PVector[] vert = new PVector[4];
  int[][] faces;

  // constructor
  Tetrahedron(float radius) {
    this.radius = radius;
    a = radius*0.6666;
    vert[0] = new PVector( a, a, a );  // vertex 1
    vert[1] = new PVector(-a, -a, a );    // vertex 2
    vert[2] = new PVector(-a, a, -a );  // vertex 3
    vert[3] = new PVector( a, -a, -a );   // vertex 4
  }

  // draws tetrahedron 
  void create() {
    super.create();
    beginShape(TRIANGLE_STRIP);
    vertex(vert[0].x, vert[0].y, vert[0].z);  // vertex 1
    vertex(vert[1].x, vert[1].y, vert[1].z);    // vertex 2
    vertex(vert[2].x, vert[2].y, vert[2].z);  // vertex 3
    vertex(vert[3].x, vert[3].y, vert[3].z);   // vertex 4
    vertex(vert[0].x, vert[0].y, vert[0].z);  // vertex 1
    vertex(vert[1].x, vert[1].y, vert[1].z);    // vertex 2
    vertex(vert[3].x, vert[3].y, vert[3].z);   // vertex 4
    vertex(vert[2].x, vert[2].y, vert[2].z);  // vertex 3
    vertex(vert[1].x, vert[1].y, vert[1].z);    // vertex 2
    endShape(CLOSE);
  }
}

class Hexahedron extends PlatonicSolid {

  // Tetrahedron
  float x, y, z;
  float radius;
  float a;
  PVector[] vert = new PVector[8];
  int[][] faces;

  // constructor
  Hexahedron(float radius) {
    this.radius = radius;

    a = radius/1.1414;
    faces = new int[6][4];
    vert[0] = new PVector(  a, a, a );
    vert[1] = new PVector(  a, a, -a );
    vert[2] = new PVector(  a, -a, -a );
    vert[3] = new PVector(  a, -a, a );
    vert[4] = new PVector( -a, -a, a );
    vert[5] = new PVector( -a, a, a );
    vert[6] = new PVector( -a, a, -a );
    vert[7] = new PVector( -a, -a, -a );

    faces[0] = new int[] {0, 1, 2, 3};
    faces[1] = new int[] {4, 5, 6, 7};
    faces[2] = new int[] {0, 3, 4, 5};
    faces[3] = new int[] {1, 2, 7, 6};
    faces[4] = new int[] {2, 3, 4, 7};
    faces[5] = new int[] {0, 5, 6, 1};
  }

  // draws hexahedron 
  void create() { 
    super.create();
    for (int i=0; i<6; i++)
    {
      beginShape();
      for (int j=0; j<4; j++)
      {
        vertex(vert[faces[i][j]].x, vert[faces[i][j]].y, vert[faces[i][j]].z);
      }
      endShape();
    }
  }
}

class Octahedron extends PlatonicSolid {

  // Octahedron
  float x, y, z;
  float radius;

  float a;
  PVector[] vert = new PVector[6];
  int[][] faces;

  // constructor
  Octahedron(float radius) {
    this.radius = radius;
    a = radius;
    vert[0] = new PVector( a, 0, 0 ); 
    vert[1] = new PVector( 0, a, 0 );
    vert[2] = new PVector( 0, 0, a ); 
    vert[3] = new PVector( -a, 0, 0 ); 
    vert[4] = new PVector( 0, -a, 0 ); 
    vert[5] = new PVector( 0, 0, -a );
  }

  // draws octahedron 
  void create() {
    super.create();
    beginShape(TRIANGLE_FAN); 
    vertex(vert[4].x, vert[4].y, vert[4].z);
    vertex(vert[0].x, vert[0].y, vert[0].z);
    vertex(vert[2].x, vert[2].y, vert[2].z);
    vertex(vert[3].x, vert[3].y, vert[3].z);
    vertex(vert[5].x, vert[5].y, vert[5].z);
    vertex(vert[0].x, vert[0].y, vert[0].z);
    endShape();

    beginShape(TRIANGLE_FAN);    
    vertex(vert[1].x, vert[1].y, vert[1].z);
    vertex(vert[0].x, vert[0].y, vert[0].z);
    vertex(vert[2].x, vert[2].y, vert[2].z);
    vertex(vert[3].x, vert[3].y, vert[3].z);
    vertex(vert[5].x, vert[5].y, vert[5].z);
    vertex(vert[0].x, vert[0].y, vert[0].z);
    endShape();
  }
}

class Dodecahedron extends PlatonicSolid {
  // Dodecahedron
  float radius;
  float a, b, c;
  PVector[] vert;
  int[][] faces;

  // constructor
  Dodecahedron(float radius) {
    this.radius = radius;
    a = radius/1.618033989;
    b = radius;
    c = 0.618033989*a;
    faces = new int[12][5];
    vert = new PVector[20];
    vert[ 0] = new PVector(a, a, a);
    vert[ 1] = new PVector(a, a, -a);
    vert[ 2] = new PVector(a, -a, a);
    vert[ 3] = new PVector(a, -a, -a);
    vert[ 4] = new PVector(-a, a, a);
    vert[ 5] = new PVector(-a, a, -a);
    vert[ 6] = new PVector(-a, -a, a);
    vert[ 7] = new PVector(-a, -a, -a);
    vert[ 8] = new PVector(0, c, b);
    vert[ 9] = new PVector(0, c, -b);
    vert[10] = new PVector(0, -c, b);
    vert[11] = new PVector(0, -c, -b);
    vert[12] = new PVector(c, b, 0);
    vert[13] = new PVector(c, -b, 0);
    vert[14] = new PVector(-c, b, 0);
    vert[15] = new PVector(-c, -b, 0);
    vert[16] = new PVector(b, 0, c);
    vert[17] = new PVector(b, 0, -c);
    vert[18] = new PVector(-b, 0, c);
    vert[19] = new PVector(-b, 0, -c);

    faces[ 0] = new int[] {0, 16, 2, 10, 8};
    faces[ 1] = new int[] {0, 8, 4, 14, 12};
    faces[ 2] = new int[] {16, 17, 1, 12, 0};
    faces[ 3] = new int[] {1, 9, 11, 3, 17};
    faces[ 4] = new int[] {1, 12, 14, 5, 9};
    faces[ 5] = new int[] {2, 13, 15, 6, 10};
    faces[ 6] = new int[] {13, 3, 17, 16, 2};
    faces[ 7] = new int[] {3, 11, 7, 15, 13};
    faces[ 8] = new int[] {4, 8, 10, 6, 18};
    faces[ 9] = new int[] {14, 5, 19, 18, 4};
    faces[10] = new int[] {5, 19, 7, 11, 9};
    faces[11] = new int[] {15, 7, 19, 18, 6};
  }

  // draws dodecahedron 
  void create() {
    super.create();
    for (int i=0; i<12; i++)
    {
      beginShape();
      for (int j=0; j<5; j++)
      {
        vertex(vert[faces[i][j]].x, vert[faces[i][j]].y, vert[faces[i][j]].z);
      }
      endShape();
    }
  }
}