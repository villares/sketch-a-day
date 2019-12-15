void setup() { // executa só no começo
  size(600, 500, P3D); // área de desenho 3D

void draw() { // repete infinitamente
  background(255, 175, 0);
  translate(width / 2, height / 2);
  rotateY(radians(mouseX));
  caixa(10, 10, 0, 200, 100, 40);
  caixa(-100, 140, 50, 200, 100, 40);
  caixa(140, -100, -50, 200, 100, 40);

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
