from itertools import permutations

k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

answer = 0
l = len(dungeons)

for case in permutations(dungeons, l):
    p = k
    mid = 0
    print(case)

    for dungeon in case:
        if p >= dungeon[0]:
            p -= dungeon[1]
            mid += 1
        else:
            break

    if mid > answer:
        answer = mid

    if answer == l:
        break

print(answer)