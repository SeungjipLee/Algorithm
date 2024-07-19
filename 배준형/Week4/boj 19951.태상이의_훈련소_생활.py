import sys
sys_input = sys.stdin.readline
sys_write = sys.stdout.write
def minput(): return map(int, sys_input().split())

N, M = minput() # N 연병장크기, M 조교의 수 1 ~ 100,000
arr = [0] + list(minput()) 
arr_cnt = [0] * (N+2)

for _ in range(M):
    a, b, k = minput()
    arr_cnt[a] += k
    arr_cnt[b+1] += -k

for i in range(1, N+1):
    arr_cnt[i] += arr_cnt[i-1]
    arr[i] += arr_cnt[i]
    sys_write(str(arr[i]) + " ")
    

    
