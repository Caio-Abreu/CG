from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

last_time = 0

class Esfera:

    def __init__(self, radius):

        self.radius = radius

        self.lats = 100

        self.longs = 100

        self.user_theta = 0
        self.user_height = 0

        self.direction = [0.0, 2.0, -1.0, 1.0]

        self.intensity = [0.7, 0.7, 0.7, 1.0]

        self.ambient_intensity = [0.3, 0.3, 0.3, 1.0]

        self.surface = GL_FLAT

    def init(self):

        glClearColor(0.0, 0.0, 0.0, 0.0)

        self.compute_location()

        glEnable(GL_DEPTH_TEST)

        glEnable(GL_LIGHTING)

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient_intensity)

        glEnable(GL_LIGHT0)

        glLightfv(GL_LIGHT0, GL_POSITION, self.direction)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.intensity)

        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    def compute_location(self):
        x = 2 * cos(self.user_theta)
        y = 2 * sin(self.user_theta)
        z = self.user_height
        d = sqrt(x * x + y * y + z * z)

        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()
        glFrustum(-d * 0.5, d * 0.5, -d * 0.5, d * 0.5, d - 1.1, d + 1.1)

        gluLookAt(x, y, z, 0, 0, 0, 0, 0, 1)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor3f(1.0, 1.0, 1.0)

        glShadeModel(self.surface)

        self.draw()
        glutSwapBuffers()

    def draw(self):
        for i in range(0, self.lats + 1):
            lat0 = pi * (-0.5 + float(float(i - 1) / float(self.lats)))
            z0 = sin(lat0)
            zr0 = cos(lat0)

            lat1 = pi * (-0.5 + float(float(i) / float(self.lats)))
            z1 = sin(lat1)
            zr1 = cos(lat1)

            glBegin(GL_QUAD_STRIP)

            for j in range(0, self.longs + 1):
                lng = 2 * pi * float(float(j - 1) / float(self.longs))
                x = cos(lng)
                y = sin(lng)
                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr0, y * zr0, z0)
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(x * zr1, y * zr1, z1)

            glEnd()

    def special(self, key, x, y):

        if key == GLUT_KEY_UP:
            self.user_height += 0.1
        if key == GLUT_KEY_DOWN:
            self.user_height -= 0.1

        if key == GLUT_KEY_LEFT:
            self.user_theta += 0.1
        if key == GLUT_KEY_RIGHT:
            self.user_theta -= 0.1

        if key == GLUT_KEY_F1:
            if self.surface == GL_FLAT:
                self.surface = GL_SMOOTH
            else:
                self.surface = GL_FLAT

        self.compute_location()
        glutPostRedisplay()

    def idle(self):
        global last_time
        time = glutGet(GLUT_ELAPSED_TIME)

        if last_time == 0 or time >= last_time + 40:
            last_time = time
            glutPostRedisplay()

    def visible(self, vis):
        if vis == GLUT_VISIBLE:
            glutIdleFunc(self.idle)
        else:
            glutIdleFunc(None)


def main():

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowSize(300, 300)
    glutInitWindowPosition(50, 100)

    glutCreateWindow('Esfera')

    s = Esfera(1.0)

    s.init()

    glutDisplayFunc(s.display)

    glutVisibilityFunc(s.visible)

    glutSpecialFunc(s.special)

    glutMainLoop()

if __name__ == '__main__':
    main()