
class Rectangle:
    def __init__(self):
        self.__pikkus = None
        self.__laius = None

    @property
    def laius(self):
        return self.__laius

    @laius.setter
    def laius(self, laius):
        self.__laius = laius

    @property
    def pikkus(self):
        return self.__pikkus

    @pikkus.setter
    def pikkus(self, pikkus):
        self.__pikkus = pikkus

    def area(self):
        return float(self.__laius) * float(self.__pikkus)

    def perimeter(self):
        return 2 * (float(self.__laius) + float(self.__pikkus))
