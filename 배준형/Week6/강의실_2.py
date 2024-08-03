import sys, heapq
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
room_info = [0] * (N+1)
max_room = 0
arr = []
for _ in range(N):
    c, s, e = minput()
    arr.append([c, s, e])

arr.sort(key=lambda x: (x[1], x[2]-x[1]))
heap = []
max_room += 1
heapq.heappush(heap, [arr[0][2], max_room])
room_info[arr[0][0]] = max_room

for i in range(1, N):
    c, s, e = arr[i]
    if heap[0][0] <= s:
        v, num = heapq.heappop(heap)
        heapq.heappush(heap, [e, num])
        room_info[c] = num
    else:
        max_room += 1
        heapq.heappush(heap, [e, max_room])
        room_info[c] = max_room


print(max_room)
for i in range(N):
    print(room_info[i+1])
