"""
from: https://www.programiz.com/python-programming/property

Using the property decorator

"""


class  Celsius(object):
    def __init__(self, temperature=0):
        print("__init__ is called")
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("temperature() - getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("temperature() - setting value")
        self._temperature = value

c = Celsius(100)
print(c.temperature)
c.temperature = 200
print(c.temperature)

