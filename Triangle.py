from Vector3D import Vector3D
from Color import Color


class Triangle:
    points = Vector3D[3] 

    def Triangle(self, points):
        for i in range(3):
            self.points[i] = points[i]

    def Triangle(self, one, two, three):
        self.points[0] = one
        self.points[1] = two
        self.points[2] = three

    def get(self, index):
        return self.points[index]

    def getOne(self):
        return self.points[0]

    def getTwp(self):
        return self.points[1]

    def getThree(self):
        return self.points[2]

    def setOne(self, one):
        self.points[0] = one

    def setTwo(self, two):
        self.points[1] = two

    def setThree(self, three):
        self.points[2] = three

    def intersect(self, ray):
        return None


    