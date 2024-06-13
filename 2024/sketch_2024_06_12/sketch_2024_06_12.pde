PShape shp;

void setup(){
  size(300, 300);
  shp = loadShape("a.svg");
  shape(shp, 0, 0);
  PShape path = shp.getChildren()[1].getChildren()[0];
  shape(path, 0, 0);
  shape(shp, 100, 0);
  shape(shp, 0, 0);
  scale(3.5);
  path.setStroke(255);
  path.setFill(color(255, 0, 0, 10));
  shape(path, 0, 0);
}
