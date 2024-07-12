n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
res = []

def back():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    
    for i in range(n):
        res.append(ls[i])
        back()
        res.pop()

back()
