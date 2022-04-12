from Camera import Camera
from Dir_Light import Dir_Light
from Mesh import Mesh

class Scene:
    def Scene(self, light = Dir_Light(0,0,0), cam = Camera(0,0,0,0), mesh = Mesh()):
        self.light = light
        self.cam = cam
        self.mesh = mesh

        ##NEED WORK