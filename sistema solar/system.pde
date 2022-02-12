float theta = 0;

void setup() {
  size(480, 270);
}

void draw() {
  background(255);
  stroke(0);

  translate(width/2, height/2);
  fill(255, 200, 50);
  ellipse(0, 0, 64, 64);

  pushMatrix();
  rotate(theta);
  translate(100, 0);
  fill(50, 200, 255);
  ellipse(0, 0, 32, 32);

  pushMatrix(); 
  rotate(-theta*4);
  translate(36, 0);
  fill(50, 255, 200);
  ellipse(0, 0, 12, 12);
  popMatrix();

  popMatrix();

  theta += 0.01;
}
