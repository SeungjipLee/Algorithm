from collections import defaultdict

def solution(genres, plays):
    answer = []
    set_genres = set(genres)
    g_id = {g: idx for idx, g in enumerate(set_genres)}
    played = [[0, []] for g in set_genres]
    n = len(genres)
    for i in range(n):
        played[g_id[genres[i]]][0] += plays[i]
        played[g_id[genres[i]]][1].append([plays[i], i])
    played.sort(key=lambda x: x[0], reverse=True)
    for play in played:
        play = sorted(play[1], key=lambda x: x[1])
        play = sorted(play, key=lambda x: x[0], reverse=True)
        # print(play)
        for p in play[:2]:
            answer.append(p[1])
    return answer