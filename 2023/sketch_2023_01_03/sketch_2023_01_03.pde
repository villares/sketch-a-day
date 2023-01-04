// Para criar imagem com glitch a partir de 
// arquivo JPG na sub-pasta /data 

PImage img;
int n = 10;  // número de passos estragando bytes!
String nomeArquivo = "sesc.jpg";

void setup() {
  size(382, 510);
  noLoop();
}

void draw() {
  byte[] data=loadBytes(nomeArquivo);    // carrega a imagem original
  for (int i = 0; i < n; i++) {
    int loc=(int)random(1, data.length);  // sorteia uma posição no array
    data[loc]=(byte)random(255);          // sorteia um valor de byte e substitui
  }
  saveBytes("gliched_" + nomeArquivo, data);         // salva um novo arquivo modificado
  img = loadImage("gliched_" + nomeArquivo);        // carrega a imagem modificada
  image (img, 0, 0);
}

void keyPressed() {
  saveFrame("###.png");
  redraw();
}
