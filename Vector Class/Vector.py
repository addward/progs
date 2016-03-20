class Vector:
    def __init__(self,a):
        self.koord = a
        self.len = len(a)
    def __add__(self, b):
        if (self.len == b.len):
            new = Vector(self.koord)
            for i in range(b.len):
                new.koord[i] = self.koord[i]+b.koord[i]
            return new
        else:
            print ("Error")
            Vector.koord="Error"
            return Vector
    def __sub__(self, b):
        if (self.len == b.len):
            new = Vector(self.koord)
            for i in range(b.len):
                new.koord[i] = self.koord[i] - b.koord[i]
            return new
        else:
            print ("Error")
            Vector.koord="Error"
            return Vector
    def __mul__(self, b):
        if (self.len==b.len):
            new = Vector(self.koord)
            for i in range(b.len):
                new.koord[i]=self.koord[i]*b.koord[i]
            return new
        else:
            print ("Error")
            Vector.koord='Error'
            return Vector
