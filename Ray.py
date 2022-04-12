from Vector3D import Vector3D
class Ray:
    def Ray(self, origin=Vector3D(0, 0, 0), direction=Vector3D(0, 0, 0)):
        self.origin = origin
        self.direction = direction