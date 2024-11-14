from collections import deque

# n = int(input())
# cards = list(map(int, input().split()))
'''
[0] + [6,7,8,8,5,6,7,8,9,10,2,3,4,11]
cnt = 0
cur = cards[0]
for i in range(1, n+1):
    if cards[i] > i:
        cnt = 0
        continue
    
    if cur <= cards[i]:
        cnt += 1
    else:
        cnt = 0
'''
cards = [0] + [6,7,8,8,5,6,6,7,8,8,9,10,12,11,15,2,3,4,5,6,7,8,9,10,11]
queue = deque(cards)
cur = 1
cnt = 0
while queue:
    x = queue.popleft()
    if x == cur:
        cur += 1
    else:
        cnt += 1

print(cnt)