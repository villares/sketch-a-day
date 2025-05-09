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
    translate(x, y);
    for (int i = 2; i < n; i = i + 2) {
      noStroke();
      fill(dna.genes[i-1], 1, 1, dna.genes[i+2]);
      float x1 = map(dna.genes[i], 0, 1, -wh/4, wh/4);
      float y1 = map(dna.genes[i+1], 0, 1, -wh/4, wh/4);
      float x2 = map(dna.genes[i*2], 0, 1, -wh/4, wh/4);
      float y2 = map(dna.genes[i*2+1], 0, 1, -wh/4, wh/4);
      float x3 = map(dna.genes[i-1], 0, 1, wh/10, wh/4);
      float y3 = map(dna.genes[i*2-1], 0, 1, wh/10, wh/4);
      triangle(x1, y1, x2, y2, x3, y3);
    }
    // Draw the bounding box
    pushStyle();
    if (mouseIsOver) fill(0, 0.25);
    else noFill();
    rectMode(CENTER);
    stroke(1);
    rect(0, 0, wh, wh);
    popStyle();
    popMatrix();

    // Display fitness value
    textAlign(CENTER);
    fill(1);
    text(fitness, x, y+70);
  }

  float getFitness() {
    return fitness;
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
}
