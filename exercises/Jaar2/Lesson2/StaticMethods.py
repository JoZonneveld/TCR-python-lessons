class DegreesCalC:
    @staticmethod
    def celsius_to_fahrenheit(temp):
        return temp * 1.8 + 32

    @staticmethod
    def celsius_to_kelvin(temp):
        return temp + 273.15

    @staticmethod
    def fahrenheit_to_celsius(temp):
        return (temp - 32) / 1.8

    @staticmethod
    def fahrenheit_to_kelvin(temp):
        return (temp + 459.67) * (5 / 9)

    @staticmethod
    def kelvin_to_celsius(temp):
        return temp - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(temp):
        return temp * 1.8 - 459.67


print(DegreesCalC.celsius_to_fahrenheit(15))
print(DegreesCalC.celsius_to_kelvin(15))

print(DegreesCalC.fahrenheit_to_celsius(59))
print(DegreesCalC.fahrenheit_to_kelvin(59))

print(DegreesCalC.kelvin_to_celsius(288.15))
print(DegreesCalC.kelvin_to_fahrenheit(288.15))


