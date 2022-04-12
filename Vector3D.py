import math


class Vector3D:
    def Vector3D(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def Vector3D(self, x,y,z):
        self(float(x), float(y), float(z))

    def Vector3D(self, vector3D):
        self.x = vector3D.x
        self.y = vector3D.y
        self.z = vector3D.z


    def plus(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def scale(self, scale):
        return Vector3D(self.x * scale, self.y * scale, self.z * scale)

    def minus(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def lengthSqr(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def length(self):
        return float(math.sqrt(self.lengthSqr))

    def normalize(self):
        length = self.length()
        toReturn = Vector3D(self.x/length, self.y/length, self.z/length)
        return toReturn

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x1 = self.y * other.z - self.z * other.y
        y1 = self.z * other.x - self.x * other.z
        z1 = self.x * other.y - self.y * other.x
        return Vector3D(x1,y1,z1)

    def negate(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def clamp(self, min, max):
        toReturn = Vector3D(self)
        toReturn.x = math.max(0, math.min(1, toReturn.x))
        toReturn.y = math.max(0, math.min(1, toReturn.y))
        toReturn.z = math.max(0, math.min(1, toReturn.z))

        return toReturn

    def reflect(self, about):
        dot = self.dot(about)
        negation = self.scale(-1)
        toReturn = negation.plus(about.scale(2*dot))
        return toReturn





    def __str__(self):#NOT SURE WHAT FOR
        return "x: %.2f y: %.2f z: %.2f" % (self.x, self.y, self.z)

    
