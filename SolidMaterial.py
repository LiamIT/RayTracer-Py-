from Dir_Light import Dir_Light
from Material import Material
from Vector3D import Vector3D


class SolidMaterial(Material):
    def SolidMaterial(self, color = Vector3D(0,0,0)):
        self.color = color

    def Shade(self, fromDir = Vector3D(0,0,0), position = Vector3D(0,0,0), normal = Vector3D(0,0,0), directionalLight = Dir_Light(0,0)):
        return self.color