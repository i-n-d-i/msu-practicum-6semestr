import math
from sys import stdin


class BooleanFunction:
    def __init__(self, truth_table):
        if isinstance(truth_table, list) is False:
            raise TypeError("Truth table is not a list")
        if len(truth_table) == 0 or math.log(len(truth_table), 2).is_integer() is False:
            raise ValueError("Truth table length is not a power of two")
        for elem in truth_table:
            if elem != 1 and elem != 0:
                raise ValueError("Truth table values must be either 0 or 1")
        self.truth_table = truth_table
        self.size = int(math.log(len(truth_table), 2))          # к-во переменных

    def __str__(self):
        size = int(math.log(len(self.truth_table), 2))
        array = []
        for i in range(size):
            array.append("x" + str(i + 1))
        return f"f{'(%s)'%', '.join(map(str, array))} = {tuple(self.truth_table)}"

    def __call__(self, object):
        if isinstance(object, list) is False:
            raise TypeError("Function argument is not a list")
        if len(object) != self.size:
            raise ValueError("Arity mismatch")
        for elem in object:
            if elem != 1 and elem != 0:
                raise ValueError("Variable values must be either 0 or 1")
        object = '%s' % ''.join(map(str, object))
        num = int(object, 2)
        return self.truth_table[num]

    def __add__(self, other):
        if type(other) != BooleanFunction:
            raise TypeError(f"Must be BooleanFunction, not {type(other).__name__}")
        elif other.size != self.size:
            raise ValueError("Arity mismatch")
        else:
            array = [0] * len(self.truth_table)
            for i in range(len(self.truth_table)):
                array[i] = self.truth_table[i] ^ other.truth_table[i]
            return BooleanFunction(array)

    def __mul__(self, other):
        if type(other) != BooleanFunction:
            raise TypeError(f"Must be BooleanFunction, not {type(other).__name__}")
        elif other.size != self.size:
            raise ValueError("Arity mismatch")
        else:
            array = [0] * len(self.truth_table)
            for i in range(len(self.truth_table)):
                array[i] = self.truth_table[i] and other.truth_table[i]
            return BooleanFunction(array)


def main():
    exec(stdin.read())


if __name__ == "__main__":
    main()
