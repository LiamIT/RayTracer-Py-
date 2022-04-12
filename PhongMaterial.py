import math
from Dir_Light import Dir_Light
from Material import Material
from Vector3D import Vector3D

class PhongMaterial:
    def PhongMaterial(self, color = Vector3D(0,0,0)):
        self.color = color

    def Shade(self, fromDirection = Vector3D(0,0,0), position = Vector3D(0,0,0), normal = Vector3D(0,0,0), directionalLight = Dir_Light(0,0)):
        ambient = Vector3D(float(.1), float(.1), float(.1))

        diffuseStrength = normal.normalize().dot(directionalLight.dirToLight.normalize())
        diffuseStrength = math.max(0, diffuseStrength)

        diffuse = self.color.scale(diffuseStrength)


        reflection = directionalLight.dirToLight.reflect(normal)
        specularStrength = math.max(0, reflection.dot(fromDirection))
        specularStrength = float(math.pow(specularStrength, 2))

        specular = Vector3D(float(1), float(1), float(1)).scale(specularStrength)

        finalColor = ambient.plus(diffuse).plus(specular)
        finalColor = finalColor.clamp(0, 1)

        return finalColor