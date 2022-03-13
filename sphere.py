import numpy
from PIL import Image
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from png import Reader


def read_texture(filename, texture_unit):
    # PIL can open BMP, EPS, FIG, IM, JPEG, MSP, PCX, PNG, PPM
    # and other file types.  We convert into a texture using GL.
    print('trying to open', filename)
    try:
         image = Image.open(filename)
    except IOError as ex:
        print('IOError: failed to open texture file ', filename)
        sys.exit()
        return -1
    print('opened file: size=', image.size, 'format=', image.format)
    imageData = numpy.array(list(image.getdata()), numpy.uint8)
    reader = Reader(filename='E:\\Codes_WebModerno\\Computação Grafica\\mapa.png')
    w, h, pixels, metadata = reader.read_flat()
    glActiveTexture(GL_TEXTURE0 + texture_unit)
    texture_obj = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glBindTexture(GL_TEXTURE_2D, texture_obj)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, imageData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

    image.close()
    return texture_obj


angle = 0


def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    angle += 0.1
    glScalef(1, 1, -1)

    gluQuadricTexture(quadratic_obj, GL_TRUE)
    gluSphere(quadratic_obj, 1, 50, 50)
    glPopMatrix()

    glDisable(GL_TEXTURE_2D)

    glutSwapBuffers()
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow(b"OpenGL Window")
glutDisplayFunc(display)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(40, 1, 1, 40)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
gluLookAt(0, 4, 0, 0, 0, 0, 0, 0, 1)

glEnable(GL_LIGHTING)
glLightfv(GL_LIGHT0, GL_POSITION, [-10, 10, 4, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 1, 0.8, 1])
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
glEnable(GL_LIGHT0)

texture_id = read_texture('E:\\Codes_WebModerno\\Computação Grafica\\mapa.png', 0)
quadratic_obj = gluNewQuadric()

glutMainLoop()

gluDeleteQuadric(quadratic_obj)

exit()
