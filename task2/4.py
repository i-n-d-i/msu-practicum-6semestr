from sys import stdin


def decorator_with_func(func):
    def wrapper(self, *args):
        print("Так сказать")
        return func(self, *args)
    return wrapper


class FindLozhkin(type):
    def __new__(cls, name, bases, namespace):
        if "lozhkin" in namespace:
            if isinstance(namespace["lozhkin"], int) is True:
                if namespace["lozhkin"] < 10**9:
                    namespace["lozhkin"] = 10**9
            elif isinstance(namespace["lozhkin"], str) is True:
                namespace["lozhkin"] = "Так сказать, " + namespace["lozhkin"]
            elif callable(namespace["lozhkin"]):
                namespace["lozhkin"] = decorator_with_func(namespace["lozhkin"])
        else:
            raise TypeError("Очень плохой класс, в нём нет Ложкина")
        return type.__new__(cls, name, bases, namespace)


def main():
    exec(stdin.read())


if __name__ == "__main__":
    main()
