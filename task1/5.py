import re
import sys


def main():
    tmp = re.compile(r"^0b((0|1)+)$")
    all_lines = []
    for line in sys.stdin:
        line = line.rstrip()
        example = re.search(tmp, line)
        if example is not None:
            if line in all_lines:
                print("ALREADY SEEN")
            else:
                answer = int(example.group(1), 2)
                print(f"{answer:X}")
        else:
            print("NOT MATCH")
        all_lines.append(line)


if __name__ == "__main__":
    main()
