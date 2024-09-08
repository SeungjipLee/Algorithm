w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())


# 편도
if ((p+t) // w) % 2 == 1:
    x = w - (p+t) % w
# 왕복
else:
    x = (p+t) % w


# 편도
if ((q+t) // h) % 2 == 1:
    y = h - (q+t) % h
# 왕복
else:
    y = (q+t) % h

print(x, y)