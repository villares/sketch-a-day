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

  // Create a new organism
  Organism(DNA dna_, float x_, float y_) {
    dna = dna_;
    x = x_; 
    y = y_;
    fitness = 1;
  }

  // Display the organism
  void display() {
    // We are using the organism's DNA to pick properties for this organism
    // Now, since every gene is a floating point between 0 and 1, we map the values
    int n  = int(map(dna.genes[0]+dna.genes[39], 0, 2, 3, 19)); 
    pushMatrix();
    pushStyle();
    translate(x, y);
    for (int i = 2; i < n; i = i + 2) {
      stroke(1);
      fill(dna.genes[i-1], 1, 1);
      //noFill();
      float x1 = map(dna.genes[i], 0, 1, -wh/4, wh/4);
      float y1 = map(dna.genes[i+1], 0, 1, -wh/4, wh/4);
      float x2 = map(dna.genes[i*2], 0, 1, -wh/4, wh/4);
      float y2 = map(dna.genes[i*2+1], 0, 1, -wh/4, wh/4);
      float x3 = map(dna.genes[i-1], 0, 1, wh/10, wh/4);
      float y3 = map(dna.genes[i*2-1], 0, 1, wh/10, wh/4);
      triangle(x1, y1, x2, y2, x3, y3);
    }
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
    int q1, q2, q3, q4;
    int cx = int(x-wh/2);
    int cy = int(y-wh/2);
    q1 = getNonBlack(cx, cy, int(x), int(y));
    q2 = getNonBlack(int(x),cy , cx+wh,int(y));
    q3 = getNonBlack(cx, int(y), int(x), cy+wh);
    q4 = getNonBlack(int(x), int(y), cx+wh, cy+wh);
    int t = getNonBlack(cx, cy,  cx+wh, cy+wh);
    fitness = t - abs(q1-q2) - abs(q3 - q4)  - abs(q1 - q3)  - abs(q2 - q2);
    return fitness;
  }

  DNA getDNA() {
    return dna;
  }

  int getNonBlack(int x1, int y1, int x2, int y2) {
    int count = 0;
    for (int x = x1; x < x2; x++) {
      for (int y = y1; y < y2; y++) {
        if (get(x, y) != color(0)) count++;
      }
    }
    return count;
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
}
