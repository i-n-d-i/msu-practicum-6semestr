from sys import stdin
import math


class CovidSimulator:
    def __init__(self, days, degree):
        self.days = days
        self.degree = degree
        self.temperature = 36.6
        self.current_day = 0
        self.index = 0              # к-во дней с максимальной температурой

    def __iter__(self):
        return self

    def __next__(self):
        if self.days == self.current_day:
            raise StopIteration
        if self.current_day != 0:
            tmp = round(self.temperature + self.degree, 1)
            if self.current_day < math.ceil(self.days / 2) and tmp <= 40:
                self.temperature = tmp
                if self.temperature + self.degree > 40:
                    self.index = self.days - 2 * self.current_day
                elif self.days % 2 == 0:
                    self.index = 2
            elif self.index > 1:
                self.index -= 1
            elif self.days != 2:
                self.temperature -= self.degree
        self.current_day += 1
        return self.temperature


def main():
    exec(stdin.read())


if __name__ == "__main__":
    main()
