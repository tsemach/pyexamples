"""
from: https://www.programiz.com/python-programming/property

Using property object.

Note: temperature is *not* the temprature value!, it is a "property object" which hes getter and setter.
Those setter and getter are called when the temperature's dictionary location is access.

"""


class Celsius:
    def __init__(self, temperature=0):
        print("__init__: called")
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("get_temperature() - getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("set_temperature() - setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)

c = Celsius()
c.temperature = 50
print(c.temperature)
