/*
 s180107 Platonic Solids
 (c)2018 Alexandre B A Villares
 https://abav.lugaralgum.com/sketch-a-day
 */

PlatonicSolid[] solids;
float r_x = 0;
float r_y = 0;

void setup() {
  size(500, 500, P3D);
  //strokeCap(ROUND);
  smooth();
  noStroke();
  fill(127);
  colorMode(HSB);
  //strokeWeight(3);
  //stroke(200, 0, 0);
  solids = new PlatonicSolid[100];
  for (int i = 0; i<100; i++) {
     solids[i] = PlatonicFactory((int)random(5), color(random(256),255,255));
  }
}

void draw() {
  r_x += 0.02;
  r_y += 0.01;
  background(0);
    lights();
  for (int i = 0; i<100; i++) {
    int x = x_from_i(i, 10);
    int y = y_from_i(i, 10, 10);
    pushMatrix();
    {
      translate(25 + x *50, 25 + y *50);
      pushMatrix(); 
      {
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
      }
      popMatrix();
    }
    popMatrix();
  }
  // if (frameCount < 200){ saveFrame("###.tga");}
}

int x_from_i(int idx, int max_x) { 
  return idx % max_x;
}

int y_from_i(int idx, int max_x, int max_y) {
  return (idx / max_x) % max_y;
}