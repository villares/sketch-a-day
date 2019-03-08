float x, y; // posição x, posição y
float px, py; // posição x anterior, posição y anterior
float tempoX = 0; // declarando a variável global tempoX e inicializando com 0
float tempoY = 10; // declarando a variável global tempoY e inicializando com 10

void setup() {
  size(500, 500); // define o tamanho da tela em pixels. Largura X Altura
  x = width * noise(tempoX); // calcula a posição x inicial
  y = height * noise(tempoY); // calcula a posição y inicial
}

void draw() {
  background(0);
  px = x; // guarda a posição x na variável px
  py = y; // guarda a posição y na variável py
  x = width * noise(tempoX);  // atualiza a posição x sorteando um valor
  y = height * noise(tempoY); // atualiza a posição y sorteando um valor
  olho(x, y , dist(px, py, x, y)*100); // desenha uma linha entre os pontos (px, py) e (x, y)
  // incrementa os tempos a cada frame
  tempoX = tempoX + 0.005;
  tempoY = tempoY + 0.005;
}


void olho(float x, float y, float tamanho) {
  noStroke();
  // branco    
  fill(255); 
  ellipse(x, y, tamanho, tamanho/2);
  // iris
  fill(random(256), random(256), random(256));
  ellipse(x, y, tamanho*.40, tamanho*.40);
  // pupila
  fill(0);
  ellipse(x, y, tamanho*.10, tamanho*.10);
}
