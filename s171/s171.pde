// Inpired on http://10print.org/
// s171 180619

int altura = 10;

void setup() {
  rectMode(CENTER);
  frameRate(10);
  noStroke();
  size(500, 500);
  for ( int h = 10; h < height; h = h + 20) {
    //rect(10, h, 200, 10);
  }
}
void draw() {
  //background(255);
  for (int i = 0; i < 25; i=i+1) {
    for (int j = 0; j < 25; j=j+1) {
      fill(random(256), 
        random(256), 
        random(256));
      float tam = random (10, 20);
      rect(10+j*20, 10+i*20, tam, tam);
    }
  }
}
