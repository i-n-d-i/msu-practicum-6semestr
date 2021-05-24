def decorator(name):
    def decorator_with_func(func):
        def wrapper(*args):
            for i in range(len(args)):
                print(i, ": ", args[i], sep='')
            print(name, ": ", func(*args), sep='')
        return wrapper
    return decorator_with_func


@decorator("f1")
def f1(a, b, c):
    return a + b + c


@decorator("f2")
def f2(a, b):
    return a * a + b * b


def main():
    f1(3, 4, 5)
    f2(7, 9)


if __name__ == "__main__":
    main()
