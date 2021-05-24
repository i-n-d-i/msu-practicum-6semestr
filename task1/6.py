import sys


def function():
    index = 1
    line = yield
    while True:
        line *= index
        index += 1
        line = yield line


def main():
    gen = function()
    next(gen)
    for line in sys.stdin:
        line = line.rstrip()
        print(gen.send(line))


if __name__ == "__main__":
    main()
