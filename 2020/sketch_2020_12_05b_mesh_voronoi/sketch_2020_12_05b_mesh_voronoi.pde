import megamu.mesh.*;
float[][] points = new float[3][2];

void setup() { 
  size(400, 400);
}

void draw() {
  points[0][0] = mouseX; // first point, x
  points[0][1] = mouseY; // first point, y
  points[1][0] = 150; // second point, x
  points[1][1] = 105; // second point, y
  points[2][0] = 320; // third point, x
  points[2][1] = 113; // third point, y  
  Voronoi myVoronoi = new Voronoi( points );
  // getRegions() returns an array of MPolygons,
  // the order of which correspond to the order of
  // the points entered. MPolygon contains the points
  // of the polygon, and can be drawn to the stage.;
  MPolygon[] myRegions = myVoronoi.getRegions();
  for (int i=0; i<myRegions.length; i++)
  {
    // an array of points
    float[][] regionCoordinates = myRegions[i].getCoords();
    fill(64 + i * 64, 0, 0);
    myRegions[i].draw(this); // draw this shape
  }
}
