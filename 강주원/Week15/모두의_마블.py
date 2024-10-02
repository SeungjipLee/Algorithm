n = int(input())
ls = list(map(int, input().split()))
print(sum(ls) + (len(ls)-2)*max(ls))