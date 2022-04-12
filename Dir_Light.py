from Vector3D import Vector3D

class Dir_Light:
    dirToLight = Vector3D(0, 0, 0)
    intensity = 0.0

    def __init__(self, dirToLight, intensity):
        self.dirToLight= dirToLight
        self.intensity = intensity

    #keep an eye on...not sure if I translated it right
    def normalize(self):
        self.dirToLight = self.dirToLight.normalize()
        return self