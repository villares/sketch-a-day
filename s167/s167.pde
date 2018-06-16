//  Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
String SKETCH_NAME = "s167"; // 180615

import peasy.*;

PeasyCam cam;
ArrayList<PVector> pontos; 
float space;

void setup() {
  size(600, 600, P3D);
  noStroke();
  strokeWeight(2);
  cam = new PeasyCam(this, 100);
  cam.setMinimumDistance(100);
  cam.setMaximumDistance(1000);

  pontos = new ArrayList<PVector>();

  int gridDim = 10;
  space = width / gridDim;
  for (int ix =0; ix< gridDim; ix++) {
    for (int iy=0; iy< gridDim; iy++) {
      for (int iz=0; iz< gridDim; iz++) {
        float x = space/2 + ix * space - width/2 + random(-2, 2);
        float y = space/2 + iy * space - width/2 + random(-2, 2);
        float z = space/2 + iz * space - width/2 + random(-2, 2);
        pontos.add(new PVector(x, y, z));
      }
    }
  }
}
void draw() {
  background(200);
  for (PVector p : pontos) {
    pushMatrix();
    translate(p.x, p.y, p.z);
    fill(0);
    noStroke();
    box(4);
    popMatrix();
    for (PVector op : pontos) {
      stroke(200, 0, 100);
      if (dist(p.x, p.y, p.z, op.x, op.y, op.z) < space) {
        line(p.x, p.y, p.z, op.x, op.y, op.z);
      }
    }
  }
}
