//  Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
String SKETCH_NAME = "s167"; // 180615

import peasy.*;

PeasyCam cam;
ArrayList<PVector> points; 
ArrayList<PVector[]> lines; 

float space;

void setup() {
  size(600, 600, P3D);
  cam = new PeasyCam(this, 300);
  cam.setMinimumDistance(100);
  cam.setMaximumDistance(1000);

  points = new ArrayList<PVector>();
  lines = new ArrayList<PVector[]>();

  int gridDim = 10;
  space = width / gridDim;
  for (int ix =0; ix< gridDim; ix++) {
    for (int iy=0; iy< gridDim; iy++) {
      for (int iz=0; iz< gridDim; iz++) {
        float x = space/2 + ix * space - width/2 + random(-2, 2);
        float y = space/2 + iy * space - width/2 + random(-2, 2);
        float z = space/2 + iz * space - width/2 + random(-2, 2);
        points.add(new PVector(x, y, z));
      }
    }
  }
  for (PVector p : points) {
    for (PVector op : points) {
      if (dist(p.x, p.y, p.z, op.x, op.y, op.z) < space) {
        lines.add(new PVector[]{p, op});
      }
    }
  }
}


void draw() {
  //rotateY(frameCount/1000.);
  background(200);
  for (PVector p : points) {
    pushMatrix();
    translate(p.x, p.y, p.z);
    fill(0);
    noStroke();
    box(4);
    popMatrix();
  }
  for (PVector[] l : lines) {
    strokeWeight(2);
    stroke(200, 0, 100);
    line(l[0].x, l[0].y, l[0].z, l[1].x, l[1].y, l[1].z);
  }
  //if (frameCount/31.4 <= TWO_PI) {
  //  saveFrame("s###.png");
  //} else { 
  //  exit();
  //}
}
