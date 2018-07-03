// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com
// Interactive Selection
// http://www.genarts.com/karl/papers/siggraph91.html

// The class for our "organism", contains DNA sequence, fitness value, position on screen
// Fitness Function f(t) = t (where t is "time" mouse rolls over organism)

class Organism {

  DNA dna;          // organism's DNA
  float fitness;    // How good is this organism?
  float x, y;       // Position on screen
  int wh = 110;      // Size of square enclosing organism
  boolean mouseIsOver; // Are we rolling over this organism?
  PVector[] points;

  // Create a new organism
  Organism(DNA dna_, float x_, float y_) {
    dna = dna_;
    x = x_; 
    y = y_;
    fitness = 1;
    points = new PVector[6];
    println(points.length );
  }

  // Display the organism
  void display() {
    // We are using the organism's DNA to pick properties for this organism
    // Now, since every gene is a floating point between 0 and 1, we map the values

    pushMatrix();
    pushStyle();
    translate(x, y);
    beginShape();
    for (int i = 0; i < 12; i = i + 2) {
      float px = map(dna.genes[i], 0, 1, -wh/4, wh/4);
      float py = map(dna.genes[i+1], 0, 1, -wh/4, wh/4);
      vertex(px, py);
      points[i/2] = new PVector(px, py);
    }
    endShape(CLOSE);

    // Draw the bounding box
    popStyle();

    rectMode(CENTER);

    if (mouseIsOver) stroke(0, 1, 1);
    else stroke(1);
    noFill();
    rect(0, 0, wh, wh);
    stroke(0.5);
    line(-wh/2, 0, wh/2, 0);
    line(0, -wh/2, 0, wh/2);
    popMatrix();


    // Display fitness value
    getFitness();
    textAlign(CENTER);
    fill(1);
    text(fitness, x, y+70);
  }

  float getFitness() {
    int cx = int(x-wh/2);
    int cy = int(y-wh/2);
    int t = getNonBlack(cx, cy, cx+wh, cy+wh);
    fitness = t/100;
    return  fitness;
  }

  DNA getDNA() {
    return dna;
  }



  // Increment fitness if mouse is rolling over organism
  void checkMouseOver(int mx, int my) {
    int cx = int(x-wh/2);
    int cy = int(y-wh/2);

    if (mx > cx && mx < cx + wh  && my > cy && my < cy + wh) {
      mouseIsOver = true;
      if (mousePressed) fitness += 0.25;
    } else {
      mouseIsOver = false;
    }
  }

  //float pArea(PVector p[])
  //{ 
  //  float area = 0;
  //  float x0 = p[0].x;
  //  float  y0= p[0].y;
  //  for (int i = 1; i < p.length; i++) {
  //    area += p[i].x*x0- p[i].y*y0;
  //    x0 = p[i].x;
  //    y0 = p[i].y;
  //  }
  //  return abs(area/2);
  //}

  //float pLen(PVector p[])
  //{ 
  //  float len = 0;
  //  float x0 = p[0].x;
  //  float  y0= p[0].y;
  //  for (int i = 1; i < p.length; i++) {
  //    len += dist(p[i].x, p[i].y, x0, y0);
  //  }
  //  return len;
  //}


  int getNonBlack(int x1, int y1, int x2, int y2) {
    int count = 0;
    for (int x = x1; x < x2; x++) {
      for (int y = y1; y < y2; y++) {
        if (get(x, y) != color(0)) count++;
      }
    }
    return count;
  }
}
