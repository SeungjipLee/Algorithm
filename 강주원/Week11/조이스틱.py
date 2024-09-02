n = int(input())
a,b,c = 0, 0, 0
a = n//300
n %= 300
b = n//60
n %= 60
c = n//10
n %= 10
if n == 0:
    print(a,b,c)
else:
    print(-1)