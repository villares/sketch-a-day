// Based on Stackoverflow C# rounded corner post 
// https://stackoverflow.com/questions/24771828/algorithm-for-creating-rounded-corners-in-a-polygon

void setup() {
  size(500, 500);
}

void draw() {
  background(200);
  PVector p1 = new PVector(100, 400);
  PVector  p0 = new PVector(300, 100);
  PVector  p2 = new PVector(mouseX, mouseY);
  float r = 50;
  roundedCorner(p0, p1, p2, r);
}

void roundedCorner(PVector angularPoint, 
  PVector p1, PVector p2, float radius)
{
  //Vector 1
  float dx1 = angularPoint.x - p1.x;
  float dy1 = angularPoint.y - p1.y;

  //Vector 2
  float dx2 = angularPoint.x - p2.x;
  float dy2 = angularPoint.y - p2.y;

  //Angle between vector 1 and vector 2 divided by 2
  float angle = (atan2(dy1, dx1) - atan2(dy2, dx2)) / 2;

  // The length of segment between angular point and the
  // points of intersection with the circle of a given radius
  float tan = abs(tan(angle));
  float segment = radius / tan;

  //Check the segment
  float length1 = GetLength(dx1, dy1);
  float length2 = GetLength(dx2, dy2);

  float length = min(length1, length2);

  if (segment > length)
  {
    segment = length;
    radius = (float)(length * tan);
  }

  // Points of intersection are calculated by the proportion between 
  // the coordinates of the vector, length of vector and the length of the segment.
  PVector p1Cross = GetProportionPoint(angularPoint, segment, length1, dx1, dy1);
  PVector p2Cross = GetProportionPoint(angularPoint, segment, length2, dx2, dy2);

  // Calculation of the coordinates of the circle 
  // center by the addition of angular vectors.
  float dx = angularPoint.x * 2 - p1Cross.x - p2Cross.x;
  float dy = angularPoint.y * 2 - p1Cross.y - p2Cross.y;

  float L = GetLength(dx, dy);
  float d = GetLength(segment, radius);

  PVector circlePoint = GetProportionPoint(angularPoint, d, L, dx, dy);

  //StartAngle and EndAngle of arc
  float startAngle = atan2(p1Cross.y - circlePoint.y, p1Cross.x - circlePoint.x);
  float endAngle = atan2(p2Cross.y - circlePoint.y, p2Cross.x - circlePoint.x);

  //Sweep angle
  float sweepAngle = endAngle - startAngle;

  //Some additional checks
  if (sweepAngle < 0)
  {
    startAngle = endAngle;
    sweepAngle = -sweepAngle;
  }

  if (sweepAngle > PI)
    sweepAngle = PI - sweepAngle;

  //Draw result using graphics
  noFill();
  strokeWeight(3);
  line(p1.x, p1.y, p1Cross.x, p1Cross.y);
  line(p2.x, p2.y, p2Cross.x, p2Cross.y);
  arc(circlePoint.x, circlePoint.y, 2 * radius, 2 * radius, 
    startAngle, startAngle + sweepAngle);
}

float GetLength(float dx, float dy)
{
  return sqrt(dx * dx + dy * dy);
}

PVector GetProportionPoint(
  PVector point, float segment, 
  float L, float dx, float dy)
{
  float factor;
  if (L !=0) {
    factor = segment / L;
  } else { 
    factor = 0;
  }
  return new PVector(
    (float)(point.x - dx * factor), 
    (float)(point.y - dy * factor));
}
