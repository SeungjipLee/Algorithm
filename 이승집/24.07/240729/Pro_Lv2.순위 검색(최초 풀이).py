def solution(info, query):
    save = []
    answer = []

    for i in info:
        lan, fr_ba, se_ju, food, score = i.split()
        save.append([lan, fr_ba, se_ju, food, int(score)])

    for i in query:
        fi_lan, fi_fr_ba, fi_se_ju, k = i.split(" and ")
        fi_food, fi_score = k.split()
        mid = len(info)
        mid_save = save[:]

        # 1. 언어 거르기
        if fi_lan == "-":
            pass
        else:
            mid2_save = []
            for j in mid_save:
                if j[0] != fi_lan:
                    mid -= 1
                else:
                    mid2_save.append(j)
            mid_save = mid2_save[:]
        if mid == 0:
            answer.append(0)
            continue
        # 2. 직무 거르기
        if fi_fr_ba == "-":
            pass
        else:
            mid2_save = []
            for j in mid_save:
                if j[1] != fi_fr_ba:
                    mid -= 1
                else:
                    mid2_save.append(j)
            mid_save = mid2_save[:]
        if mid == 0:
            answer.append(0)
            continue
        # 3. 경력 거르기
        if fi_se_ju == "-":
            pass
        else:
            mid2_save = []
            for j in mid_save:
                if j[2] != fi_se_ju:
                    mid -= 1
                else:
                    mid2_save.append(j)
            mid_save = mid2_save[:]
        if mid == 0:
            answer.append(0)
            continue
        # 4. 음식 거르기
        if fi_food == "-":
            pass
        else:
            mid2_save = []
            for j in mid_save:
                if j[3] != fi_food:
                    mid -= 1
                else:
                    mid2_save.append(j)
            mid_save = mid2_save[:]
        if mid == 0:
            answer.append(0)
            continue
        # 5. 점수 거르기
        if fi_score == "-":
            pass
        else:
            mid2_save = []
            for j in mid_save:
                if int(j[4]) < int(fi_score):
                    mid -= 1
                else:
                    mid2_save.append(j)
            mid_save = mid2_save[:]
        if mid == 0:
            answer.append(0)
            continue

        answer.append(mid)
    return answer


"""
완전탐색으로 풀었으나 메모리도, 시간도 너무 많이 잡아먹음
"""