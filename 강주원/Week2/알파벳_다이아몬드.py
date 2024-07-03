n, r1, c1, r2, c2 = map(int, input().split())
ls = [chr(i) for i in range(97,123)]
length = n*2-1
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        temp = abs(n-i%length-1) + abs(n-j%length-1)
        if temp > n-1:
            print(".", end = "")
        else:
            print(ls[temp%26], end = "")
    print()