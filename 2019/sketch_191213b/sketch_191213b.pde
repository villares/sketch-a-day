int seed;

void setup() {
  size(800, 300, P3D); 
  frameRate(10);
  seed = 26876; //novaSemente();
}

void draw() {
  lights();
  background(0);
  randomSeed(seed);
  translate(width/2, height/2);
  rotateY(radians(mouseX));
  translate(-width/2, -height/2);
  for (int y=30; y<height; y+=30) {
    for (int x=30; x<width; x+=30) {
      float tamanho = random(5, 25);
      fill(corSorteada());
      caixa(x, y, 0, tamanho);
    }
  }
}

void keyPressed() {
  if (key == ' ') {
    seed = novaSemente();
  }
}

int novaSemente() {
  int s = int(random(1000000));
  println("seed: " + s);
  return s;
}

color corSorteada(){
  return color(random(256), random(256), random(256));
}

void caixa(float x, float y, float z, 
  float w, float h, float d) {
  pushMatrix();
  translate(x, y, z);
  box(w, h, d);
  popMatrix();
}

void caixa(float x, float y, float z, float lado) {
  caixa(x, y, z, lado, lado, lado);
}
