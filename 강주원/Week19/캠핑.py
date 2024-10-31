import sys
input = sys.stdin.readline

cnt = 1
while 1:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    
    res = v // p * l + min(l, v % p)
    print(f'Case {cnt}: {res}')
    cnt += 1

'''
5 8 20
11111000 11111000 1111

1 4 6
1000 10
'''