from abc import ABC, abstractmethod
from sys import stdin


class NormalForm(ABC):
    def __init__(self):
        self.clause = []

    def add_clause(self, object):
        if isinstance(object, list) is False:
            raise TypeError("Not a list")
        for elem in object:
            if isinstance(elem, int) is False:
                raise TypeError("Not an int")
            if elem == 0:
                raise ValueError("Element == 0")
        self.clause.append(object)

    @staticmethod
    def check_values(object):
        if isinstance(object, dict) is False:
            raise TypeError("Not a dict")
        for key in object.keys():
            if isinstance(key, int) is False or isinstance(object[key], int) is False:
                raise TypeError("Not an int")
            if key < 1:
                raise ValueError("Key < 1")
            if object[key] != 0 and object[key] != 1:
                raise ValueError("Value not in {0, 1}")

    @abstractmethod
    def __call__(self, object):
        var_values = new_list(self.clause)
        for i in range(len(self.clause)):
            for j in range(len(self.clause[i])):
                tmp = self.clause[i][j]
                if tmp >= 0:
                    if tmp not in object:
                        raise ValueError(f"Variable {tmp} is not found")
                    var_values[i][j] = object[tmp]
                else:
                    tmp = -tmp
                    if tmp not in object:
                        raise ValueError(f"Variable {tmp} is not found")
                    var_values[i][j] = not object[tmp]
        return var_values


def new_list(lists):
    new_list = []
    for list in lists:
        clause = []
        for elem in list:
            clause.append(0)
        new_list.append(clause)
    return new_list


class DNF(NormalForm):
    def __init__(self):
        super().__init__()

    def __call__(self, object):
        super().check_values(object)
        var_values = super().__call__(object)
        clause_values = [1] * len(self.clause)
        answer = 0
        for i in range(len(var_values)):
            for j in range(len(var_values[i])):
                clause_values[i] = clause_values[i] and var_values[i][j]
        for elem in clause_values:
            answer = answer or elem
        return int(answer)


class CNF(NormalForm):
    def __init__(self):
        super().__init__()

    def __call__(self, object):
        super().check_values(object)
        var_values = super().__call__(object)
        clause_values = [0] * len(self.clause)
        answer = 1
        for i in range(len(var_values)):
            for j in range(len(var_values[i])):
                clause_values[i] = clause_values[i] or var_values[i][j]
        for elem in clause_values:
            answer = answer and elem
        return int(answer)


def main():
    exec(stdin.read())


if __name__ == "__main__":
    main()
