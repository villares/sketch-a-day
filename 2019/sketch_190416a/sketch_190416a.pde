// Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
// Some basic Processing 3D tips

void setup() {
  size(500, 500, P3D); // the most essentian thing!
  rectMode(CENTER);
  // this may cause performance issues
  hint(ENABLE_DEPTH_SORT); // helps with translucent faces 
}

void draw() {
  // ortho(); // changes projection - must be on draw()!
  background(200);
  // It's common to have origin at center
  translate(width/2, height/2);
  // lousy orbit  
  rotateY(radians(mouseX));
  rotateX(radians(mouseY));
  // now some drawing
  strokeWeight(2);
  fill(255, 100);
  // you can draw 2D stuff in 3D!
  rect(0, 0, 100, 200);
  // lines can be (x1, y1, z1, x2, y2, z2)
  line(50, 100, 0, 0, 0, 50);
  // some boxes!
  translate(0, 0, 20);
  box(10);
  translate(0, 0, 20);
  box(30, 20, 10);
}
