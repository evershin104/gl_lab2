from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Func for window
def changeSize(w, h):
    if h == 0:
        h = 1
    ratio = w * 1.0 / h
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, w, h)
    gluPerspective(45, ratio, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

# Renders scene with pyramid and cube
def renderScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, -8, 5, 0, 0, 0, 0, -1, 0)
    pyramid()
    cube()
    glutSwapBuffers()


def pyramid():
    glTranslate(-3, -1, 0)
    glRotate(20, -1, 1, 1)
    # Right side
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex3f(0.5, 1, 0)

    glColor3f(0, 0, 1)
    glVertex3f(1, 0, 0)

    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 1.5)
    glEnd()

    # Left side
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex3f(0.5, 1, 0)

    glColor3f(0, 0, 1)
    glVertex3f(-1, 0, 0)

    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 1.5)
    glEnd()

    # Back side
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)
    glVertex3f(-1, 0, 0)

    glColor3f(0, 0, 1)
    glVertex3f(1, 0, 0)

    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 1.5)
    glEnd()

    # Down side
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex3f(0.5, 1, 0)

    glColor3f(0, 0, 1)
    glVertex3f(1, 0, 0)

    glColor3f(0, 0, 1)
    glVertex3f(-1, 0, 0)
    glEnd()

    #glTranslate(-3, -1, 0)
    #glRotate(20, -1, 1, 1)

def cube():
    glTranslate(3, 1.5, 1)
    glRotate(30, 1, 1, 1)
    # Front
    glColor3f(0, 0, 1)
    glBegin(GL_QUADS)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glEnd()

    # Upper
    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glEnd()

    # Down
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glEnd()

    # Left
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glEnd()

    # Right
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glEnd()

    # Back
    glColor3f(0.2, 0.1, 0.8)
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glEnd()



glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowPosition(10, 10)
glutInitWindowSize(900, 600)
window = glutCreateWindow("OpenGL")
glutDisplayFunc(renderScene)
glutReshapeFunc(changeSize)
glEnable(GL_DEPTH_TEST)
glutMainLoop()
