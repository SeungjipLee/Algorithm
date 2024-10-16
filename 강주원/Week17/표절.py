n = int(input())
ls = sorted(list(map(int, input().split())))

def binary_search(start, end, init_):
    check = -1
    while start <= end:
        mid = (start+end) // 2        
        if ls[mid] * 0.9 > init_:
            end = mid - 1
        else:
            start = mid + 1
            check = mid

    return check - i


res = 0
visit = {}
for i in range(n-1):
    I = ls[i]
    if visit.get(I) == None:
        a = binary_search(i+1, n-1, I)
        if a > -1:
            visit[I] = a
        else:
            continue
    else:
        visit[I] -= 1
        a = visit[I]

    res += a 

print(res)