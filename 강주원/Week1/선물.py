N, L, W, H = map(int, input().split())
s, e = 0, max(L, W, H)
for _ in range(100):
    m = (s+e)/2
    if (L//m)*(W//m)*(H//m) >= N:
        s = m
    else:
        e = m
print("%.10f" %(e))