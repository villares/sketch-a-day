PImage img;
PImage imgTemp;
int i = 0;


void setup() {
  size(100, 100);
  img = loadImage("a.jpg");
  imgTemp = img.get();
  surface.setSize(img.width * 2, img.height);
}
void draw() {
  if (i < imgTemp.pixels.length) {
    float record = -1; 
    int selectedPixel = i; 
    for (int j = i; j < imgTemp.pixels.length; j++) {
      color pix   = imgTemp.pixels[j]; 
      float b = hue(pix); 
      if (b > record) {
        selectedPixel = j; 
        record = b;
      }
    }
    color cor = imgTemp.pixels[i];
    imgTemp.pixels[i] = imgTemp.pixels[selectedPixel];
    imgTemp.pixels[selectedPixel] = cor;
  i++;
  }
  imgTemp.updatePixels();
  image(img, 0, 0);
  image(imgTemp, img.width, 0);
}
