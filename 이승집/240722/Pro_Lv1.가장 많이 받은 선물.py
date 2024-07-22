friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

gift_index = {i: 0 for i in friends}

k = len(friends)
friend_idx = {friends[i]: i for i in range(k)}
gift_board = [[0]* len(friends) for _ in range(k)]

for i in gifts:
    send, recieve = i.split()
    gift_board[friend_idx[send]][friend_idx[recieve]] += 1
    gift_index[send] += 1
    gift_index[recieve] -= 1

next_gift = [0] * k

for i in range(k):
    for j in range(i, k):
        if i != j:
            # 비교
            if gift_board[i][j] > gift_board[j][i]:
                next_gift[i] += 1
            elif gift_board[i][j] < gift_board[j][i]:
                next_gift[j] += 1
            else:
                if gift_index[friends[i]] > gift_index[friends[j]]:
                    next_gift[i] += 1
                elif gift_index[friends[i]] < gift_index[friends[j]]:
                    next_gift[j] += 1

print(max(next_gift))