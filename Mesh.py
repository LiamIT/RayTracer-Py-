from Geometry import Geometry
from Material import Material
class Mesh:
    def Mesh(self, geometry = Geometry, material = Material):
        self.geometry = geometry
        self.material = material