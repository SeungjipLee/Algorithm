"""
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
"""
import heapq

n = int(input())
min_heap = []

for _ in range(n):
    row = list(map(int, input().split()))
    for num in row:
        if len(min_heap) < n:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        print(min_heap)
    print("--------------------")

print(min_heap[0])