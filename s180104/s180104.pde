/*
s180104 Tetrahedrons
(c)2018 Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
*/

Tetrahedron[] thList;
float rot_x = 0;
float rot_y = 0;

void setup() {
  int numTh = 400;
  thList = new Tetrahedron[numTh];
  size(500, 500, P3D);
  noStroke();
  for (int i = 0; i < numTh; i++) {
    float x = random(0, width);
    float y = random(0, height);
    float z = random(-500, 0);
    Tetrahedron t = new Tetrahedron(x, y, z, 40); // instancia um tetrah
    thList[i] = t ; // acrescenta na lista
  }
}

void draw() {
  background(128);
  for (int i = 0; i < thList.length; i++) { 
    thList[i].plot();
  }
  // if (frameCount < 100){ saveFrame("##.png"); }
}

class Tetrahedron {
  float x, y, z, radius, rot_x, rot_y;
  boolean showFaces;
  PVector[] vert = new PVector[5];
  Tetrahedron(float x_, float y_, float z_, float radius_) {
    x = x_;
    y = y_;
    z = z_;
    radius = radius_;
    rot_x = random(-0.03,0.03);
    rot_y = random(-0.03,0.03);
    float a = radius*2/3;
    vert[0] = new PVector( a, a, a ); // vertex 1
    vert[1] = new PVector(-a, -a, a ); // vertex 2
    vert[2] = new PVector(-a, a, -a ); // vertex 3
    vert[3] = new PVector( a, -a, -a ); // vertex 4
  }
 // draws tetrahedron 
  void plot() {
    color c = color(map(x, 0, width, 0, 255), 
                    map(y, 0, height, 0, 255), 
                    map(z, -500, 500, 255, 0), 100);
    fill(c);
    pushMatrix();
    translate(x, y, z);
    rotateX(rot_y * frameCount);
    rotateY(rot_x * frameCount);
    beginShape(TRIANGLE_STRIP);
    vertex(vert[0].x, vert[0].y, vert[0].z); // vertex 1
    vertex(vert[1].x, vert[1].y, vert[1].z); // vertex 2
    vertex(vert[2].x, vert[2].y, vert[2].z); // vertex 3
    vertex(vert[3].x, vert[3].y, vert[3].z); // vertex 4
    vertex(vert[0].x, vert[0].y, vert[0].z); // vertex 1
    vertex(vert[1].x, vert[1].y, vert[1].z); // vertex 2
    vertex(vert[3].x, vert[3].y, vert[3].z); // vertex 4
    vertex(vert[2].x, vert[2].y, vert[2].z); // vertex 3
    vertex(vert[1].x, vert[1].y, vert[1].z); // vertex 2
    endShape(CLOSE); 
    popMatrix();
  }
}