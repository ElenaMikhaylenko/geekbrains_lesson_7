class Cell:

    SYMBOL = "@"

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        if isinstance(other, int):
            return Cell(self.cell + other)
        elif isinstance(other, Cell):
            return Cell(self.cell + other.cell)
        raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, int):
            result = self.cell - other
        elif isinstance(other, Cell):
            result = self.cell - other.cell
        else:
            raise NotImplementedError
        if result < 0:
            return Cell(~result)
        elif not result:
            return Cell(1)
        return Cell(result)

    def __mul__(self, other):
        if isinstance(other, int):
            return Cell(self.cell * other)
        elif isinstance(other, Cell):
            return Cell(self.cell * other.cell)
        raise NotImplementedError

    def __floordiv__(self, other):
        if isinstance(other, int):
            result = self.cell // other
        elif isinstance(other, Cell):
            result = self.cell // other.cell
        else:
            raise NotImplementedError
        if not result:
            return Cell(1)
        return Cell(result)

    def __str__(self):
        return f"Cell: {self.cell}"

    def make_order(self, rows):
        result = [self.SYMBOL * rows for _ in range(self.cell // rows)]
        result.append(self.SYMBOL * (self.cell % rows))
        return "\n".join(result)


cell_1 = Cell(5)
print(cell_1)
print(cell_1.make_order(2))

cell_2 = Cell(7)
print(cell_2)
print(cell_2.make_order(5))

print(f"Add: {cell_1 + cell_2}")
print(f"Sub: {cell_1 - 9}")
print(f"Mul: {cell_1 * 3}")
print(f"Div: {cell_1 // 6}")
