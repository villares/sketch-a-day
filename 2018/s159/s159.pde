/* Exemplo de um sistema de partículas com lista dinâmica 'ArrayList' 
 * Os objetos da classe grupoDeBolas contém uma lista de bolinhas da classe Bola
 * A festa é um ArrayList de grupoDeBolas (uma lista de grupos de bolinhas)
 */

String SKETCH_NAME  = "s159"; // 180608
String OUTPUT = ".gif"  ;

import gifAnimation.*;
GifMaker gifExporter;

ArrayList<grupoDeBolas> festa; // festa é uma lista de grupos de bolas

void setup() {
  size(500, 500);
  noStroke();
  festa = new ArrayList<grupoDeBolas>(); // inicializa a festa
  for (int i = 0; i < 20; i++) {
    festa.add(new grupoDeBolas(random(width), random(height-width/4, height), 150));
  }
  gifExporter = new GifMaker(this, SKETCH_NAME + OUTPUT);
  gifExporter.setRepeat(0);
  gifExporter.setDelay(170);
}

void draw() {
  background(100);
  for (grupoDeBolas grupo : festa) {  // para cada lista da festa
    grupo.update();
  }

  for (int i = festa.size()-1; i >= 0; i--) {  // percorre a festa, do fim para o começo
    grupoDeBolas grupo = festa.get(i);  // pega um grupo
    int numBolas = grupo.bolas.size();   // bê quantas bolas o grupo tem
    if (numBolas == 0) {                // se o grupo estiver vazio
      festa.remove(i);                  // remove o grupo da festa
      //println(festa.size());
    }
  }
  gifExporter.addFrame();
  if (festa.size() == 0) {
    gifExporter.finish();
    exit();
  }
}

void mousePressed() {
  festa.add(new grupoDeBolas(mouseX, mouseY, 150));
}

class Bola {
  float x, y, vx, vy, tamanho;
  color cor;
  Bola(float px, float py, float tam_min, float tam_max) {
    x = px;
    y = py;
    tamanho = random(tam_min, tam_max);
    colorMode(HSB);
    cor = color(random(100, 200), 255, 255);
    vx = random(-2, 2);
    vy = random(-6, -2);
    //println(vy);
  }
  void plot() {
    fill(cor);
    ellipse ( x, y, tamanho, tamanho);
  }
  void update() {
    // reduz o tamanho 
    tamanho = tamanho * .99;
    // atualiza a posição x
    x = x + vx;
    // rebate nas laterais do canvas
    if (x < 0 || x > width) { 
      vx = -vx;
    }
    // "gravidade" 
    vy = vy + 0.035;
    // atualiza a posição y
    y = y + vy;
    // rebate no topo do canvas
    if (y < 0) { 
      vy = -vy;
    }
  }
}

class grupoDeBolas {
  ArrayList<Bola> bolas;  // lista de bolas do grupo
  // construtor
  grupoDeBolas(float px, float py, int num) {
    bolas = new ArrayList<Bola>();
    for (int i = 0; i < num; i++) {
      bolas.add(new Bola(px, random(py-5, py+5), 5, 20));
    }
  }

  void update() {
    for (Bola bola : bolas) {
      bola.plot();  
      bola.update();
    }
    // remove bolas que ficaram muito pequenas
    for (int i = bolas.size()-1; i >= 0; i--) { 
      Bola bola = bolas.get(i);
      if (bola.tamanho < 1) {
        bolas.remove(i);
        //println(i);
      }
    }
  }
}
