from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

a = 0

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1),
         (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    raio = 2
    N = 5
    H = 4
    pontosBase = []
    pontosbase2 =[]
    angulo = (2*math.pi)/N

    glPushMatrix()
    elapsed_seconds = glutGet(GLUT_ELAPSED_TIME) / 1000
    glRotatef(elapsed_seconds * 90, 3, 1, 1)
    glColor3fv(cores[0])

    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)
        pontosBase += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for i in range(0,N):
        m = raio * math.cos(i*angulo)
        n = raio * math.sin(i*angulo)
        pontosbase2 += [ (m,n) ]
        glVertex3f(m,n,H)
    glEnd()

    glBegin(GL_QUADS)
    for i in range(0,N):
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(pontosBase[i][0],pontosBase[i][1],0.0)
        glVertex3f(pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
        #glVertex3f(pontosBase[i][0],pontosBase[i][1],H)
        glVertex3f(pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],H)
        glVertex3f(pontosbase2[i][0],pontosbase2[i][1],H)
    glEnd()
    glPopMatrix()

    glutSwapBuffers()
    glutPostRedisplay()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 0.1, 10.0)
    glMatrixMode(GL_MODELVIEW)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(400, 300)
glutCreateWindow(b"OpenGl Window")
glutReshapeFunc(reshape)
glutDisplayFunc(display)

glClearColor(0.0, 0.0, 0.0, 1.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslate(0, 0, -5)
glEnable(GL_DEPTH_TEST)

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

#glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0)) # directional light from the front
# point light from the left, top, front
glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

glutMainLoop()
