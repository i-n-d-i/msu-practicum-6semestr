def func(len):
    lst = [0] * len
    while lst[0] != 2:
        yield tuple(lst)
        lst[len - 1] += 1
        for i in range(len - 1, 0, -1):
            if lst[i] == 2:
                lst[i] = 0
                lst[i - 1] += 1


def main():
    n = int(input())
    if n == 1:
        print('(0)')
        print('(1)')
    else:
        for f in func(n):
            print(f)


if __name__ == "__main__":
    main()
