// PlatonicSolid ico, tet, oct, dod, hex, p;
PlatonicSolid[] solids;
float r_x = 0;
float r_y = 0;

void setup() {
  size(500, 500, P3D);
  strokeCap(ROUND);
  smooth();
  solids = new PlatonicSolid[100];
  for (int i = 0; i<100; i++) {
    switch((int)random(5)) {
    case 0:  
      solids[i] = new Tetrahedron(18, 0, false); 
      break;
    case 1:  
      solids[i] = new Hexahedron(14, 0, false);
      break;
    case 2:  
      solids[i] = new Octahedron(22, 0, false);    
      break;
    case 3:  
      solids[i] = new Dodecahedron(18.0, 0, false);    
      break;
    case 4:  
      solids[i] = new Icosahedron(18, 0, false);    
      break;
    }
  }
  //tet = new Tetrahedron(30, 0, false);
  //hex = new Hexahedron(23, 0, false);
  //oct = new Octahedron(37, 0, false);
  //dod = new Dodecahedron(30, 0, false);
  //ico = new Icosahedron(30, 0, false);
}

void draw() {
  r_x += 0.02;
  r_y += 0.01;
  background(0);
  lights();
  stroke(200, 0, 0);
  strokeWeight(3);

  for (int i = 0; i<100; i++) {
    int x = x_from_i(i, 10, 10);
    int y = y_from_i(i, 10, 10);
    pushMatrix();
    translate(25 + x *50, 25 + y *50);

    pushMatrix(); 
    pushStyle();
    if (dist(mouseX, mouseY, 25 + x *50, 25 + y *50)<25) {
      scale(2);
      translate(0, 0, 30);
      stroke(255);
    }
    rotateX(r_y);
    rotateY(r_x);
    solids[i].create();
    popStyle();
    popMatrix();
    popMatrix();
  }


  //pushMatrix();
  //translate(100, height*.25, 0);
  //rotateX(r_y);
  //rotateY(r_x);
  //p.create();
  //popMatrix();

  //pushMatrix();
  //translate(200, height*.25, 0);
  //rotateX(r_y);
  //rotateY(r_x);
  //hex.create();
  //popMatrix();

  //pushMatrix();
  //translate(300, height*.25, 0);
  //rotateX(r_y);
  //rotateY(r_x);
  //oct.create();
  //popMatrix();

  //pushMatrix();
  //translate(400, height*.25, 0);
  //rotateX(r_y);
  //rotateY(r_x);
  //dod.create();
  //popMatrix();

  //pushMatrix();
  //translate(500, height*.25, 0);
  //rotateX(r_y);
  //rotateY(r_x);
  //ico.create();
  //popMatrix();
}


int x_from_i(int idx, int max_x, int max_y) {
  int x =  idx % max_x;
  return x;
}

int y_from_i(int idx, int max_x, int max_y) {
  idx /= max_x;
  int y = idx % max_y;
  return y;
}