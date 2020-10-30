from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def consumption_tissue(self):
        ...


class Coat(Clothes):

    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value <= 0:
            raise Exception(value)
        self._size = value

    def consumption_tissue(self):
        return self._size / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, height):
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise Exception(value)
        self._height = value

    def consumption_tissue(self):
        return 2 * self._height + 0.3


coat = Coat(42)
costume = Costume(165)

print(f"{coat.consumption_tissue():.2f}")
print(costume.consumption_tissue())
