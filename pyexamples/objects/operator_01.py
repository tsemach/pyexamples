"""
<description>
                                                                                             
</description>
<output>
C1 = (4, 2)
C2 = (-3, 3)
C1 + C2 = (1, 5)
C1 - C2 = (7, -1)
C1 = (4, 2)
C2 = (-3, 3)
C1 + C2 = (-18, 6)
C1 = (4, 2)
C2 = (-3, 3)
C3 = (-18, 6)
(-54, 18)
C3 = (-18, 6)
</output>
"""


class Complex(object):
    def __init__(self, r, i):
        self._r = r
        self._i = i

    @property
    def image(self):
        return self._i

    @image.setter
    def image(self, i):
        return Complex(self.real, i)

    @property
    def real(self):
        return self._r

    @real.setter
    def real(self, r):
        return Complex(r, self.image)

    def __eq__(self, o):
        return o.real == self.real and o.image == self.image

    def __add__(self, o):
        real = self.real + o.real
        image = self.image + o.image

        return Complex(real, image)

    def __sub__(self, o):
        real = self.real - o.real
        image = self.image - o.image

        return Complex(real, image)

    def __mul__(self, o):
        ac = self.real * o.real
        bd = self.image * o.image
        bc = self.image * o.real
        ad = self.real * o.image

        return Complex(ac - bd, bc + ad)

    def __rmul__(self, o):
        real = self.real * o
        image = self.image * o

        return Complex(real, image)

    def __str__(self):
        return "({}, {})".format(self._r, self._i)


C1 = Complex(4, 2)
C2 = Complex(-3, 3)
print(f'C1 = {C1}')
print(f'C2 = {C2}')
print(f'C1 + C2 = {C1 + C2}')
print(f'C1 - C2 = {C1 - C2}')
print(f'C1 = {C1}')
print(f'C2 = {C2}')
print(f'C1 + C2 = {C1 * C2}')
print(f'C1 = {C1}')
print(f'C2 = {C2}')
C3 = C1 * C2
print(f'C3 = {C3}')
print(3 * C3)
print(f'C3 = {C3}')

