// bRigid provides classes for an easier handling of jBullet in Processing. bRigid is thought as a kind of Processing port for the bullet physics simulation library written in C++. 
// This library allows the interaction of rigid bodies in 3D. Geometry/ Shapes are build with Processing PShape Class, for convinient display and export (c) 2013 Daniel Köhler, daniel@lab-eds.org

//here: basic example (Box) for using rigidShapes

import javax.vecmath.Vector3f;
import peasy.*;
import bRigid.*;
import com.bulletphysics.collision.narrowphase.ManifoldPoint;
import com.bulletphysics.collision.narrowphase.PersistentManifold;

PeasyCam cam;

BPhysics physics;
BBox box;

public void settings() {
  size(1280, 720, P3D);
}

void setup() {
  colorMode(HSB);
  frameRate(60);
  cam = new PeasyCam(this, 600);

  //extends of physics world
  Vector3f min = new Vector3f(-250, -250, -250);
  Vector3f max = new Vector3f(250, 250, 250);
  //create a rigid physics engine with a bounding box
  physics = new BPhysics(min, max);
  //set gravity
  physics.world.setGravity(new Vector3f(0, 500, 0));

  //create the first rigidBody as Box or Sphere
  //BBox(PApplet p, float mass, float dimX, float dimY, float dimZ)
  //box = new BBox(this, 1, 25, 25, 25);
}

void draw() {
  background(255);
  lights();
  //rotateY(frameCount*.01f);

  if (keyPressed && frameCount % 2 == 0) {
    Vector3f pos = new Vector3f(0, -150, random(1));
    //reuse the rigidBody of the sphere for performance resons
    //BObject(PApplet p, float mass, BObject body, Vector3f center, boolean inertia)
    float side = random(10, 25);
    box = new BBox(this, 1, side, side, side);
    BObject r = new BObject(this, 100, box, pos, true);
    r.displayShape.setFill(color(side * side * side / 60, 200, 200));
    //add body to the physics engine
    physics.addBody(r);
  }
  //update physics engine every frame
  physics.update();
  // default display of every shape
  physics.display();
  //for (BObject b : physics.rigidBodies){
  //  b.display();
  //  PShape s = b.displayShape;
  //}
  //if (mousePressed) {  
  //  noStroke();
  //  physics.display();
  //} else {
  //  strokeWeight(3);
  //  stroke(0, 200, 200);
  //  getCollisionPoints();
  //}
}

void getCollisionPoints() {

  int numManifolds = physics.world.getDispatcher().getNumManifolds();
  for (int i = 0; i < numManifolds; i++) {
    PersistentManifold contactManifold = physics.world.getDispatcher().getManifoldByIndexInternal(i);
    int numCon = contactManifold.getNumContacts();

    for (int j = 0; j < numCon; j++) {
      Vector3f pos0 = new Vector3f();
      ManifoldPoint p0 = contactManifold.getContactPoint(j);
      p0.getPositionWorldOnA(pos0);        
      point(pos0.x, pos0.y, pos0.z);
    }
  }
}
