def binom(n, k):
    C = []
    for i in range(n + 1):
        C.append([0] * (k + 1))
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j] + C[i - 1][j - 1]
    return C[n][k]


def main():
    n, k = map(int, input().split())
    print(binom(n, k))


if __name__ == "__main__":
    main()
