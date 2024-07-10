n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
res = []

def back(depth):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    
    for i in range(n):
        res.append(ls[i])
        back(depth+1)
        res.pop()


back(0)
