players = ["mumu", "soe", "poe", "kai", "mine"]
callings =["kai", "kai", "mine", "mine"]

answer = []

rate = dict()

for i in range(len(players)):
    rate[players[i]] = i

print(rate)

for winner in callings:
    num_win = rate[winner]
    num_lose = num_win - 1

    rate[players[num_lose]] += 1
    rate[winner] -= 1

    players[num_win] = players[num_lose]
    players[num_lose] = winner

print(players)