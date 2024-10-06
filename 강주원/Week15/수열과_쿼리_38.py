import sys
input = sys.stdin.readline

m = int(input())
total_sum = 0
total_xor = 0


def sol(order):
    global total_sum, total_xor
    if order[0] == '1':
        total_sum += int(order[1])
        total_xor ^= int(order[1])
    elif order[0] == '2':
        total_sum -= int(order[1])
        total_xor ^= int(order[1])
    elif order[0] == '3':
        print(total_sum)
    else:
        print(total_xor)


for _ in range(m):
    sol(input().split())
