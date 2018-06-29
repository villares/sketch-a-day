// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

// Interactive Selection
// http://www.genarts.com/karl/papers/siggraph91.html

Population population;

void setup() {
  size(750, 750);
  colorMode(HSB, 1.0);
  int popmax = 25;
  float mutationRate = 0.01;  // A pretty high mutation rate here, our population is rather small we need to enforce variety
  // Create a population with a target phrase, mutation rate, and population max
  population = new Population(mutationRate, popmax);
}

void draw() {
  background(0);
  // Display the faces
  population.display();
  population.rollover(mouseX, mouseY);
  // Display some text
  textAlign(LEFT);
  fill(1);
  text("[pressione 'e' para a calcular a próxima geração] Geração #:" + population.getGenerations(), 25, 20);
}

// If 'e' is presses, evolve next generation
void keyPressed() {
  if (key == 'e') {
    randomSeed(frameCount);
    population.selection();
    population.reproduction();
    //saveFrame(population.getGenerations()+"GA.png");
  }
}
