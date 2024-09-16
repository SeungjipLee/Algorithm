import sys
input = sys.stdin.readline

def merge_sort(A, p, r):
    if (p < r):
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    global cnt, res
    i, j, tmp = p, q+1, []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1

    for idx in range(len(tmp)):
        A[p+idx] = tmp[idx]
        cnt += 1
        if cnt == m:
            res = tmp[idx]
            return

n, m = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0
res = -1
merge_sort(ls, 0, n-1)
print(res)