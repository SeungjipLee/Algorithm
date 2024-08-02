from collections import deque
import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_())

arr = [list(minput()) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[2]-x[1]))

classes = [0] * (N+1)

for i in range(N):
    n, s, e = arr[i]

    for i in range(N):
        if s >= classes[i]:
            classes[i] = e
            break
    
for i in range(N):
    if classes[i] == 0:
        print(i)
        break
# 시간 초과
# from collections import deque
# import sys
# input_ = sys.stdin.readline
# def minput(): return map(int, input_().split())

# N = int(input_())

# arr = [list(minput()) for _ in range(N)]
# arr.sort(key=lambda x: (x[1], x[2]-x[1]))

# q = deque()
# for i in range(N):
#     q.append(arr[i])
# tmp_q = deque()
# answer = 0

# while True:
#     if not q and not tmp_q:
#         break

#     cur = 0
#     if q:
#         answer += 1
#     while q:
#         n, s, e = q.popleft()
#         if s < cur:
#             tmp_q.append([n, s, e])
#         else:
#             cur = e
    
#     cur = 0
#     if tmp_q:
#         answer += 1
#     while tmp_q:
#         n, s, e = tmp_q.popleft()
#         if s < cur:
#             q.append([n, s, e])
#         else:
#             cur = e

# print(answer)