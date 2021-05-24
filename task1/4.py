import json


def unwrap(lst, ans):
    if isinstance(lst, list):
        for lst_tmp in lst:
            unwrap(lst_tmp, ans)
    else:
        ans.append(lst)


def main():
    data = json.loads(input())
    ans = []
    unwrap(data, ans)
    print(ans)


if __name__ == "__main__":
    main()
