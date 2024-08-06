# N개의 정수가 차례대로 주어진다
# 정수를 하나 받을 때마다 지금까지 받은 수 중 중간값을 출력하라
# 짝수면 작은 수

# 현재 배열에서 lowerbound 찾아서 삽입하고.. 중간값 출력하면 될듯?
# 삽입 빠르게 하려면 연결리스트 써야하고
# lowerbound 찾으려면 정렬된 배열이어야 하고
import sys
import heapq
input_ = sys.stdin.readline

N = int(input_())

minheap = []
maxheap = []

for i in range(1, N+1):
    num = int(input_())

    heapq.heappush(minheap, num)
    
    val = heapq.heappop(minheap)
    heapq.heappush(maxheap, -val)

    if i % 2 == 1:
        val = heapq.heappop(maxheap)
        heapq.heappush(minheap, -val)

    
    if i % 2 == 0:
        print(-maxheap[0])
    else:
        print(minheap[0])

    # print(maxheap, minheap)
    
