from Vector3D import Vector3D
class Camera:
    def __init__(self, origin=Vector3D(0, 0, 0),
        lookAt=Vector3D(0, 0, 1),
        lookUp=Vector3D(0, 0, 0),
        halfWidth = 0.0):
        self.origin = origin
        self.lookAt = lookAt
        self.lookUp = lookUp
        self.halfWidth = halfWidth
