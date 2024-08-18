n = int(input())
ls = sorted(list(map(int, input().split())))


if n % 2 == 0:
    print(ls[n//2-1])
else:
    print(ls[n//2])