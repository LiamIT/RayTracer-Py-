from Geometry import Geometry
from Vector3D import Vector3D
from TAndNormal import TAndNormal
from Ray import Ray

class Plane(Geometry):
    def Plane(self, ABC = Vector3D(1,0,0), dist = 0.0):
        self.ABC = ABC
        self.dist = dist

    def intersect(self, ray = Ray()):
        num = -self.dist-self.ABC.dot(ray.origin)
        den = self.ABC.dot(ray.direction)
        T = num/den
        return TAndNormal(T, self.ABC)

    #def normal_at(self, point):
    #    return self.ABC