from vector import Vector
from math import cos, sin, pi, radians


class OutOfBounds(Exception):
    pass

def deg_to_vec(deg):
    x = cos(radians(deg % 360))
    y = sin(radians(deg % 360))
    return Vector(x, y).normalized()

def distance_between(obj1, obj2):
    return abs(obj1.pos - obj2.pos)
