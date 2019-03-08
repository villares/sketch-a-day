//  Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
String SKETCH_NAME = "s166"; // 180614

import peasy.*;

PeasyCam cam;
ArrayList<PVector> pontos; 
float space;

void setup() {
  size(600, 600, P3D);
  colorMode(HSB);
  noStroke();
  cam = new PeasyCam(this, 100);
  cam.setMinimumDistance(1000);
  cam.setMaximumDistance(1000);

  // Reassign some drag handlers in order to free the left-drag to other uses
  //PeasyDragHandler orbitDH = cam.getRotateDragHandler(); // get the RotateDragHandler
  //cam.setCenterDragHandler(orbitDH);                     // set it to the Center/Wheel drag
  //PeasyDragHandler panDH = cam.getPanDragHandler();      // get the PanDragHandler
  //cam.setRightDragHandler(panDH);                        // set it to the right-button mouse drag
  //cam.setLeftDragHandler(null);                          // sets no left-drag Handler

  pontos = new ArrayList<PVector>();

  int gridDim = 20;
  space = width / gridDim;
  for (int ix =0; ix< gridDim; ix++) {
    for (int iy=0; iy< gridDim; iy++) {
      for (int iz=0; iz< gridDim; iz++) {
        float x = space/2 + ix * space - width/2;
        float y = space/2 + iy * space - width/2;
        float z = space/2 + iz * space - width/2;
        pontos.add(new PVector(x, y, z));
      }
    }
  }
}
void draw() {
  background(0);
  for (PVector p : pontos) {
    pushMatrix();
    translate(p.x, p.y, p.z);
    float noiseScale = 0.005;
    float n =  noise(abs (mouseX + p.x) *noiseScale,
                      (1000+mouseY + p.y) * noiseScale,
                     (300000+ p.z)*noiseScale);
    fill(256*n, 255, 255);
    box(space*(1-n));
    popMatrix();
  }
}
