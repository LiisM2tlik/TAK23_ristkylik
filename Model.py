from Shape import Rectangle


class Model:
    def __init__(self):
        pass

    def get_area(self, pikkus, laius):
        if not self.is_number(pikkus, laius):
            return 'Pindala arvutamiseks peavad numbrid olema positiivsed arvud!'
        rectangle = Rectangle()
        rectangle.pikkus = pikkus
        rectangle.laius = laius
        pindala = rectangle.area()
        return f'Ristküliku, mille külgede mõõdud on {pikkus} ja {laius}, pindala on: {pindala}.'

    def get_perimeter(self, pikkus, laius):
        if not self.is_number(pikkus, laius):
            return 'Ümbermõõdu arvutamiseks peavad numbrid olema positiivsed arvud!'
        rectangle = Rectangle()
        rectangle.pikkus = pikkus
        rectangle.laius = laius
        perimeter = rectangle.perimeter()
        return f'Ristküliku, mille külgede mõõdud on {pikkus} ja {laius}, ümbermõõt on: {perimeter}.'

    def is_number(self, pikkus, laius):
        try:
            float(pikkus)
            float(laius)
            if float(pikkus) <= 0 or float(laius) <= 0:
                return False
            return True
        except ValueError:
            return False

