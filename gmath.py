import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    l_color = [calculate_ambient(ambient, areflect)[n] + calculate_diffuse(light, dreflect, normal)[n] + calculate_specular(light, sreflect, view, normal)[n] for n in range(3)]
    return l_color
    
def calculate_ambient(alight, areflect):
    a_color = [int(alight[n] * areflect[n]) for n in range(3)]
    limit_color(a_color)    
    return a_color

def calculate_diffuse(light, dreflect, normal):
    normalize(normal)
    normalize(light[LOCATION])
    d = dot_product(normal, light[LOCATION])
    
    d_color = [int(light[COLOR][n] * dreflect[n] * d) for n in range(3)]
    limit_color(d_color)    
    return d_color

def calculate_specular(light, sreflect, view, normal):
    normalize(normal)
    normalize(light[LOCATION])
    normalize(view)
    s = [(normal[n] * 2 * dot_product( normal, light[LOCATION])) - light[LOCATION][n] ** SPECULAR_EXP for n in range(3)]
    s = dot_product(s, view)

    s_color = [int(light[COLOR][n] * sreflect[n] * s) for n in range(3)]
    limit_color(s_color)
    return s_color

def limit_color(color):
    color[0] = 255 if color[0] > 255 else 0 if color[0] < 0 else color[0]
    color[1] = 255 if color[1] > 255 else 0 if color[1] < 0 else color[1]
    color[2] = 255 if color[2] > 255 else 0 if color[2] < 0 else color[2]

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
