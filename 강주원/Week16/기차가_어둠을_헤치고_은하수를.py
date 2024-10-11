import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trains = [0b0 for _ in range(n+1)]


def board(train_num, sit_num):
    trains[train_num] |= (1 << sit_num-1)


def get_off(train_num, sit_num):
    trains[train_num] &= ~(1 << sit_num-1)


def back(train_num):
    trains[train_num] <<= 1
    trains[train_num] &= ((1 << 21) - 1)


def front(train_num):
    trains[train_num] >>= 1


for i in range(m):
    order = list(map(int, input().split()))
    if order[0] == 1:
        board(order[1], order[2])
    elif order[0] == 2:
        get_off(order[1], order[2])
    elif order[0] == 3:
        back(order[1])
    else:
        front(order[1])


answer = 0
visited = [False]*(2**20)
for status in trains[1:]:
    if not visited[status]:
        answer += 1
        visited[status] = True

print(answer)