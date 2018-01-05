/*

 */


var tetrah_list = [];
var rot_x = 0;
var rot_y = 0;

function setup() {
  canvas = createCanvas(500, 500, WEBGL);
  setAttributes('antialias', true);

  for (var i = -5; i < 5; i++) {
    for (var j = -5; j < 5; j++) {
      var x = i*40;
      var y = j*40;
      var z = random(-20, 20);
      var t = new Tetrahedron(x, y, z, 35, true); // instancia um tetrah
      tetrah_list.push(t);  // acrescenta na lista    }
    }
  }
}
function draw() {
  background(0);
  strokeWeight(5);
  rot_x += 0.05;
  rot_y += 0.01;
  for (var i = 0; i < tetrah_list.length; i++) { // itera pela lista apas
    tetrah_list[i].plot();
  }
}

function Tetrahedron(x, y, z, radius, showFaces) {
  this.x = x;
  this.y = y;
  this.z = z;
  this.vert = [];
  this.radius = radius;
  var a = this.radius*2/3;
  this.vert[0] = new p5.Vector( a, a, a ); // vertex 1
  this.vert[1] = new p5.Vector(-a, -a, a ); // vertex 2
  this.vert[2] = new p5.Vector(-a, a, -a ); // vertex 3
  this.vert[3] = new p5.Vector( a, -a, -a ); // vertex 4
  // draws tetrahedron 
  this.plot = function(rx, ry) {
    push();
    var tz = this.z
      if (dist(mouseX-width/2, mouseY-height/2, this.x, this.y)<50) {
      tz = tz * 10;
      stroke(0, 100, 200);
    } else {
      stroke(200, 100, 0);
    }
    translate(this.x, this.y, tz);
    rotateX(rot_y);
    rotateY(rot_x);
    line(this.vert[0].x, this.vert[0].y, this.vert[0].z, // vertex 1
      this.vert[1].x, this.vert[1].y, this.vert[1].z); // vertex 2
    line(this.vert[0].x, this.vert[0].y, this.vert[0].z, // vertex 1
      this.vert[2].x, this.vert[2].y, this.vert[2].z); // vertex 3
    line(this.vert[0].x, this.vert[0].y, this.vert[0].z, // vertex 1
      this.vert[3].x, this.vert[3].y, this.vert[3].z); // vertex 4
    line(this.vert[1].x, this.vert[1].y, this.vert[1].z, // vertex 2
      this.vert[2].x, this.vert[2].y, this.vert[2].z); // vertex 3
    line(this.vert[1].x, this.vert[1].y, this.vert[1].z, // vertex 2
      this.vert[3].x, this.vert[3].y, this.vert[3].z); // vertex 4
    line(this.vert[2].x, this.vert[2].y, this.vert[2].z, // vertex 3
      this.vert[3].x, this.vert[3].y, this.vert[3].z); // vertex 4


    pop();
  }
}
