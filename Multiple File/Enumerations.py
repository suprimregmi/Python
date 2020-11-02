# Define enumerations using ENUM base class
from enum import Enum, auto

class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    MANGO = 3
    ORANGE = 4
    PEAR = auto()
def main():
    pass

    # TODO: enums have human readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(type(repr(Fruit.APPLE)))
    # TODO: enum have name and value property
    print(Fruit.APPLE.name, Fruit.APPLE.value)
    # TODO: print autogenerated value
    print(Fruit.PEAR.value)
    # TODO: enums are hashabel - can be used as key
if __name__ == "__main__":
    main()