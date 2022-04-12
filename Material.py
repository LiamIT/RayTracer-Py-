from Vector3D import Vector3D
from Dir_Light import Dir_Light

class Material:
    Shade = Vector3D()
    Shade(lookDirection = Vector3D(), position = Vector3D(), normal = Vector3D(), directionalLight = Dir_Light())
