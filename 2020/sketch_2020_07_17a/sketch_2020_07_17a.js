// adapted from Khan Academy that adapts Dan Shiffman, natureofcode.com
// https://pt.khanacademy.org/computing/computer-programming/programming-natural-simulations/programming-particle-systems/a/particle-systems-with-forces

var gravity;
var particleSystem;
var repeller;

function setup() {
  createCanvas(400, 400);
  gravity = createVector(0, 0.2);
  particleSystem = new ParticleSystem(createVector(width / 2, 50));
  repeller = new Repeller(width / 2, 280);
}

function draw() {
  background(214, 255, 171);
  particleSystem.applyGravity();
  particleSystem.applyRepeller(repeller);
  repeller.display();
  particleSystem.addParticle();
  particleSystem.run();
  fill(0);
  text(particleSystem.particles.length, 20, 380);
};


var Repeller = function(x, y) {
  this.power = 398;
  this.position = createVector(x, y);
};

Repeller.prototype.display = function() {
  stroke(255);
  strokeWeight(2);
  fill(127);
  ellipse(this.position.x, this.position.y, 32, 32);
};

Repeller.prototype.calculateRepelForce = function(p) {
  // Calculate direction of force
  var dir = p5.Vector.sub(this.position, p.position);
  // Distance between objects
  var d = dir.mag();
  // Normalize direction vector 
  dir.normalize();
  // Keep distance within a reasonable range
  d = constrain(d, 1, 100);
  // Repelling force is inversely proportional to distance
  var force = -1 * this.power / (d * d);
  // Get force vector --> magnitude * direction
  dir.mult(force);
  return dir;
};

var Particle = function(position) {
  this.acceleration = createVector(0, 0);
  this.velocity = createVector(random(-1, 1) / 5, 0);
  this.position = position.copy();
  this.timeToLive = 255.0;
  this.mass = random(5, 20);
};

Particle.prototype.run = function() {
  this.update();
  this.display();
};

Particle.prototype.applyForce = function(force) {
  var f = force.copy();
  f.div(this.mass);
  this.acceleration.add(f);
};

Particle.prototype.update = function() {
  this.velocity.add(this.acceleration);
  this.position.add(this.velocity);
  this.acceleration.mult(0);
  this.timeToLive -= 1;
};

Particle.prototype.display = function() {
  stroke(0, 0, 0, this.timeToLive);
  strokeWeight(2);
  fill(255, 0, 0, this.timeToLive);
  ellipse(this.position.x, this.position.y, this.mass, this.mass);
};

Particle.prototype.isDead = function() {
  if (this.timeToLive < 0.0 || this.position.y > 410) {
    return true;
  } else {
    return false;
  }
};


var ParticleSystem = function(position) {
  this.origin = position.copy();
  this.particles = [];
};

ParticleSystem.prototype.addParticle = function() {
  this.particles.push(new Particle(this.origin));
};

ParticleSystem.prototype.applyForce = function(f) {
  for (var i = 0; i < this.particles.length; i++) {
    this.particles[i].applyForce(f);
  }
};

ParticleSystem.prototype.applyGravity = function() {
  for (var i = 0; i < this.particles.length; i++) {
    var particleG = gravity.copy();
    particleG.mult(this.particles[i].mass);
    this.particles[i].applyForce(particleG);
  }
};

ParticleSystem.prototype.applyRepeller = function(r) {
  for (var i = 0; i < this.particles.length; i++) {
    var p = this.particles[i];
    var force = r.calculateRepelForce(p);
    p.applyForce(force);
  }
};

ParticleSystem.prototype.run = function() {
  for (var i = this.particles.length - 1; i >= 0; i--) {
    var p = this.particles[i];
    p.run();
    if (p.isDead()) {
      this.particles.splice(i, 1);
    }
  }
};
