// Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
// Inpired on http://10print.org/
// s171 180619

int tam = 20;

void setup() {
  rectMode(CENTER);
  size(500, 500);
  noStroke();
  noLoop();
}
void draw() {
  background(0);
  int num = int(width/tam);
  for (int i = 0; i < num; i=i+1) {
    for (int j = 0; j < num; j=j+1) {
      fill(random(128), random(128), random(128));
      rect(tam/2+j*tam, tam/2+i*tam, tam, tam);
    }
  }
  for (int i = 0; i < num; i=i+1) {
    for (int j = 0; j < num; j=j+1) {
      stroke(255);
      strokeWeight(6);
      pushMatrix();      
      translate(tam/2+j*tam, tam/2+i*tam);
      rotate(HALF_PI * int(random(2)));
      line(-tam/2, -tam/2, tam/2, tam/2);
      popMatrix();
    }
  }
}
