import heapq
import sys
input = sys.stdin.readline

n = int(input())

min_heap = []
max_heap = []
for i in range(n):
    k = int(input())
    
    # max_heap 의 크기가 min_heap 보다 크거나 같게 한다
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -k)
    else:
        heapq.heappush(min_heap, k)

    if min_heap and min_heap[0] < -max_heap[0]:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    print(-max_heap[0])


