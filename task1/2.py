def main():
    N, M = map(int, input().split())
    server = {}
    for i in range(N):
        str = input()
        domen, ip = str.split(' ')
        server[domen] = ip
    for i in range(M):
        str = input()
        print(server.get(str, 'PUSTO'))


if __name__ == "__main__":
    main()
