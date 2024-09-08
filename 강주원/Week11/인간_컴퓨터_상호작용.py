import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())
l = len(s)
acc_sum = {0 : [0] * 26}

for i, ch in enumerate(s):
    acc_sum[i + 1] = acc_sum[len(acc_sum) - 1][:]
    acc_sum[i + 1][ord(ch) - 97] += 1

for i in range(n):
    target, start, end = input().rstrip().split()
    start, end = int(start), int(end)

    B = acc_sum[int(start)][ord(target) - 97]
    C = acc_sum[int(end) + 1][ord(target) - 97]
    print(C-B)