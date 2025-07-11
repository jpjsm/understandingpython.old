class Celsius:
    """
    Using property class
    - this explains the basics of property class
    - See using_property_decorator for the best practice
    """

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)

    # Only a getter, no setter (aka read-only property)
    AsFahrenheit = property(to_fahrenheit)


if __name__ == "__main__":
    human = Celsius(37)
    print(human.temperature)
    print(human.to_fahrenheit())
    try:
        human.temperature = -300
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

    print(human.AsFahrenheit)
    try:
        human.AsFahrenheit = 98.6
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
