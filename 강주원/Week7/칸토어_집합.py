import sys
input = sys.stdin.readline

def sol(num):
    if num == 1:
        return "-"
    else:
        side = sol(num//3)
        mid = " " * (num//3)
        return side + mid + side

while 1:
    try:
        n = int(input())
        res = sol(3**n)
        print(res)
    except:
        break