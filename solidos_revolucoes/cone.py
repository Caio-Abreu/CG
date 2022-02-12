from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time, sys

def drawCone( position = (0,-1,0), radius=1, height=2, slices=50,stacks=10 ):
	glPushMatrix()
	try:
		glTranslatef(*position)
		glRotatef(250, 1, 0, 0)
		glutSolidCone(radius, height, slices, stacks )
	finally:
		glPopMatrix()

def coneMaterial( ):
	glMaterialfv(GL_FRONT, GL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
	glMaterialfv(GL_FRONT, GL_DIFFUSE, GLfloat_4(0.8, 0.8, 0.8, 1.0))
	glMaterialfv(GL_FRONT, GL_SPECULAR, GLfloat_4(1.0, 0.0, 1.0, 1.0))
	glMaterialfv(GL_FRONT, GL_SHININESS, GLfloat(50.0))
def light():
	glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_4(0.0, 1.0, 0.0, 1.0))
	glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_4(1.0, 1.0, 1.0, 1.0))
	glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_4(1.0, 1.0, 1.0, 1.0))
	glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(1.0, 1.0, 1.0, 0.0));   
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
def depth():
	glDepthFunc(GL_LESS)
	glEnable(GL_DEPTH_TEST)

def display( swap=1, clear=1):
	if clear:
		glClearColor(0.5, 0.5, 0.5, 0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	x,y,width,height = glGetDoublev(GL_VIEWPORT)
	gluPerspective(
		45, 
		width/float(height or 1), 
		.25, 
		200, 
	)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(
		0,1,5, 
		0,0,0, 
		0,1,0, 
	)
	light()
	depth()
	coneMaterial()

	rotation()
	drawCone()
	if swap:
		glutSwapBuffers()

def idle( ):
	glutPostRedisplay()

starttime = time.time()

def rotation( period = 10):
	angle = (((time.time()-starttime)%period)/period)* 360
	glRotate( angle, 0,1,0)
	return angle

from OpenGL._bytes import as_8_bit
ESC = as_8_bit( '\033' )
def key_pressed(*args):
	if args[0] == ESC:
		sys.exit()

def main():
	import sys
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow('Cone')
	glutDisplayFunc(display)
	glutKeyboardFunc(key_pressed)
	glutIdleFunc(display)
	glutMainLoop()

if __name__ == "__main__":
	main()