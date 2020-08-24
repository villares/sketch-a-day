/******************
Online at https://www.openprocessing.org/sketch/948965
Based on code by Vamoss http://vamoss.com.br http://twitter.com/vamoss http://github.com/vamoss
At https://www.openprocessing.org/sketch/947367
******************/

//Em outubro de 1970, Eduardo Lopes, constando de um desenho multícomposicional: uma forma triangular permite a determinação de uma grande variedade de composições diferentes e admite aplicação em produtos variados.
//Fonte: https://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-75901971000100008&lang=pt

let size, grid, rotations;
let changed = -1;

function setup() {
  createCanvas(windowWidth, windowHeight);
  size = min(width, height) / 10;
  
  grid = [];
  rotations = [];
  let counterY = 0;
  for(let y = size/2; y < height; y += size){
    let counterX = 0;
    for(let x = size/2; x < width; x += size){
      let rotation = counterX++ % 2 == 0 ? PI / 2 : 0;
      if(counterY % 2 == 1)
        rotation += counterX % 2 == 0 ? - PI / 2 : PI / 2;
      rotations.push(rotation);
      grid.push({rotation, x, y});
    }
    counterY++;
  }
}

function draw() {
  background(255);
  grid.forEach((g, index) => {
    g.rotation += (rotations[index] - g.rotation) * 0.09; 
    push();
      translate(g.x, g.y);
      rotate(g.rotation);
      tile(size);
    pop();
  });
}

function findClosest(){
  let closest = 0;
  let closestDistance = 9999;
  grid.forEach((g, index) => {
    let d = dist(mouseX, mouseY, g.x, g.y);
    if(d < closestDistance) {
      closestDistance = d;
      closest = index;
    }
  });
  return closest;
}

function mousePressed() {
  changed = findClosest();
  rotations[changed] += TWO_PI/4;
}

function mouseMoved() {
  let tempChanged = findClosest();
  if(changed != tempChanged){
    changed = tempChanged;
    rotations[changed] += TWO_PI/4;
  }
}

function tile(s){
  push();
  translate(-s/2,-s/2);
  fill(0);
  beginShape();
  vertex(0, 0);
  bezierVertex(s / 6, s / 6, s / 2, s * 0.66, s / 2, s);
  b_arc(s, s, s, s, PI, PI+HALF_PI, 2);
  bezierVertex(s * 0.66, s / 2, s / 6, s / 6, 0, 0);
  endShape();
  pop();
}

function b_arc(cx, cy, w, h, start_angle, end_angle, mode = 0) {
  /* A bezier approximation of an arc using the
   same signature as the original Processing arc() mode 
   0 "normal" || stand-alone arc, using beginShape() and endShape()
   1 "middle" used in recursive call of smaller arcs
   2 "naked" like normal, but without beginShape() and endShape()
   for use inside a larger PShape
   */
  var px3 = 0; 
  var py3 = 0;
  var px2 = 0; 
  var py2 = 0;
  var px1 = 0; 
  var py1 = 0;
  var px0 = 0; 
  var py0 = 0;
  var theta = end_angle - start_angle;
  // Compute raw Bezier coordinates.
  if (mode != 1 || theta < HALF_PI) {
    var x0 = cos(theta / 2.0);
    var y0 = sin(theta / 2.0);
    var x3 = x0;
    var y3 = 0 - y0;
    var x1 = (4.0 - x0) / 3.0;
    var y1;
    if (y0 != 0) {
      y1 = ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0); // y0 != 0...
    } else {
      y1 = 0;
    }
    var  x2 = x1;
    var y2 = 0 - y1;
    // Compute rotationally-offset Bezier coordinates, using:
    var  bezAng = start_angle + theta / 2.0;
    var cBezAng = cos(bezAng);
    var sBezAng = sin(bezAng);
    var rx0 = cBezAng * x0 - sBezAng * y0;
    var ry0 = sBezAng * x0 + cBezAng * y0;
    var rx1 = cBezAng * x1 - sBezAng * y1;
    var ry1 = sBezAng * x1 + cBezAng * y1;
    var rx2 = cBezAng * x2 - sBezAng * y2;
    var ry2 = sBezAng * x2 + cBezAng * y2;
    var rx3 = cBezAng * x3 - sBezAng * y3;
    var ry3 = sBezAng * x3 + cBezAng * y3;
    // Compute scaled and translated Bezier coordinates.
    var rx =  w / 2.0;
    var ry = h / 2.0;
    px0 = cx + rx * rx0;
    py0 = cy + ry * ry0;
    px1 = cx + rx * rx1;
    py1 = cy + ry * ry1;
    px2 = cx + rx * rx2;
    py2 = cy + ry * ry2;
    px3 = cx + rx * rx3;
    py3 = cy + ry * ry3;
  }
  // Drawing
  if (mode == 0) {
    // 'normal' arc (not 'middle' nor 'naked')
    beginShape();
  }
  if (mode != 1) {
    // if (not 'middle'
    vertex(px3, py3);
  }
  if (abs(theta) < HALF_PI) {
    bezierVertex(px2, py2, px1, py1, px0, py0);
  } else {
    // to avoid distortion, break into 2 smaller arcs
    b_arc(cx, cy, w, h, start_angle, end_angle - theta / 2.0, 1);
    b_arc(cx, cy, w, h, start_angle + theta / 2.0, end_angle, 1);
  }
  if (mode == 0) {
    // end of a 'normal' arc
    endShape();
  }
}
