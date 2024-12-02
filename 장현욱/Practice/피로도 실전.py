# k = 피로도
# dungeons = 던전입장,소모
import itertools
def solution(k, dungeons):
    answer = 0
    # 리스트로 정렬, 순서가 다른것은 다른거로 취급
    dungeon = [list(item) for item in itertools.permutations(dungeons, len(dungeons))]

    for i in dungeon:
        count = 0
        stamina = k
        for j in i:  # 리스트 하나씩 돌아가기
            if stamina >= j[0]:
                stamina -= j[1]
                count += 1
            else:
                break
        answer = max(answer, count)
        if answer == len(dungeons):
            return answer
    return answer
