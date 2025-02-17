import sys
from itertools import combinations


def main():
    input = sys.stdin.readline

    l, c = map(int, input().split())
    letters = sorted(input().split())

    vowels = {"a", "e", "i", "o", "u"}
    for comb in combinations(letters, l):
        v = sum(ch in vowels for ch in comb)
        o = l - v

        if v >= 1 and o >= 2:
            print("".join(comb))


if __name__ == "__main__":
    main()
