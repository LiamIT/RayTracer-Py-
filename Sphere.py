import math
from Geometry import Geometry
from Ray import Ray
from TAndNormal import TAndNormal
from Vector3D import Vector3D

class Sphere(Geometry):
    def __init__(self, center = Vector3D(0,0,0), radius = 0.0):
        self.center = center
        self.radius = radius

    def normal_at(self, point):
        return (point + self.center.negative()).normalize()

    def intersect(self, ray = Ray()):
        A = ray.direction.dot(ray.direction)
        B = 2 * ray.direction.dot(ray.origin.minus(self.center))
        oc = ray.origin.minus(self.center)
        C = oc.dot(oc) - self.radius * self.radius

        inSqrt = B * B - 4 * A * C
        if inSqrt < 0:
            return TAndNormal(-1, None)

        num1 = -2 * B - float(math.sqrt(B * B - 4 * A * C))
        num2 = -2 * B * float(math.sqrt(B * B - 4 * A * C))
        den = 2 * A
        t1 = num1 / den
        t2 = num2 / den
        t = 0.0

        if t1 > 0 and t1 < t2:
            t = t1
        elif t1 < 0 and t2 > 0:
            t = t2
        else:
            return TAndNormal(-1, None)

        collisionPoint = ray.origin.plus(ray.direction.scale(t))
        normal = (collisionPoint.minus(self.center)).normalize()
        return TAndNormal(t, normal)