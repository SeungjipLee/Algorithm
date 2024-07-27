bandage = [3, 1, 5]
health = 15
attacks = [[1, 5], [2, 5], [3, 10]]

# 현재 체력
now = health
# 연속 체력 회복
connect = 0
# 가장 가까운 공격
idx = 0
# 마지막 공격시간
last = attacks[-1][0]

for time in range(1, last + 1):
    # 공격이 먼저
    if time == attacks[idx][0]:
        # 딜 들어온다(죽으면 바로 -1 리턴)
        now -= attacks[idx][1]
        if now <= 0:
            print(-1)
            break
        # 맞으면 연속 풀리고 다음 공격 대비
        connect = 0
        idx += 1
        if idx == len(attacks):
            print(now)

    else:
        # 매 시간 기본 회복
        if now + bandage[1] <= health:
            now += bandage[1]
        else:
            now = health
        # 연속 회복 시간 카운트
        connect += 1
        if connect == bandage[0]:
            connect = 0
            if now + bandage[2] > health:
                now = health
            else:
                now += bandage[2]
