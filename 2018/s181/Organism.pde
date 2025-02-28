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
  float a, ra, rl;

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
    // such as: head size, color, eye position, etc.
    // Now, since every gene is a floating point between 0 and 1, we map the values
    int d   = int(map(dna.genes[0], 0, 1, 3, 9)); // degree, number of gens
    a   = map(dna.genes[1], 0, 1, 0, HALF_PI);  // angle    
    ra   = map(dna.genes[2], 0, 1, -2, 2);      // angle randomizer

    // Once we calculate all the above properties, we use those variables to draw rects, ellipses, etc.
    pushMatrix();
    translate(x, y);
    randomSeed(int(x + y));
    branch(d, a, wh/9);
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


  void branch(int gen, float theta, float branch_size) {
    pushStyle();
    //strokeWeight(gen);
    // All recursive functions must have an exit condition!!!!
    if (gen > 0) { // and branch_size > 1:
      pushMatrix();
      stroke(map(gen,0,9,0,1), 1, 1);
      rl = map(dna.genes[3+gen], 0, 1, 0, 10);
      float h = branch_size  * (1 - random(rl/2, rl) / 15);
      rotate(theta + ra * random(1)); // Rotate by theta
      line(0, 0, 0, -h);  // Draw the branch
      translate(0, -h);  // Move to the end of the branch
      // Ok, now call myself to draw two branches!!
      pushStyle();
      branch(gen - 1, theta, h);
      popStyle();
      popMatrix();
      pushMatrix();
      h = branch_size  * (1 - random(rl/3, rl) / 15);
      rotate(-theta + ra * random(1));
      line(0, 0, 0, -h);
      translate(0, -h);
      pushStyle();
      branch(gen - 1, theta, h);
      popStyle();
      popMatrix();
    }
    popStyle();
  }
}
