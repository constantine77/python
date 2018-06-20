
class Maxmin:

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def max2(self,x,y):
        if x > y:
            return x
        return y

    def max3(self,x,y,z):
        return self.max2(x, self.max2(y,z))

