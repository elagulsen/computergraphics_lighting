from display import *
from draw import *
from parser import *
from matrix import *
import math


# lighting values
view = [0,
        0,
        1];
ambient = [38, 23, 11]
light = [[0.5,
          0.75,
          1],
         [244, 164, 100]]
areflect = [0.25,
            0.25,
            0.25]
dreflect = [0.5,
            0.5,
            0.5]
sreflect = [0.15,
            0.15,
            0.15]



screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 0, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


parse_file( 'new_script', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)
