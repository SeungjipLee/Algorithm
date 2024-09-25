# 연예인 월드컵을 진행할때, M번 연예인이 우승한다고 가정하고
# M번 연예인이 올라가면서 만나는 연예인들의 번호를 모두 구하시오
# M번 연예인 외의 인물은 매력점수가 더 높은 연예인이, 같을 경우 아이디가 더 적은 선수가 올라갑니다.
# N = [대회 참가한 연예인 번호]
# M = 우승자 번호
# A = [매력점수]

def solution(N, M, A):
    answer = []
    world_cup = list(range(1, N+1))  # 연예인들 아이디 정렬 [1, 2, 3, ...]
    how_beautiful = []  # 매력지수 기록
    for k in A:
        how_beautiful.append(k)
    
    while len(world_cup) > 1:
        now = []  # 이번 대진의 결과
        now_beautiful = []
        for i in range(0, len(world_cup), 2):  # 두명씩 비교이므로 두칸씩
            if i + 1 < len(world_cup):  # 마지막 번호의 짝이 있을때만
                if world_cup[i] == M:  # 우승자 M이 있다면
                    answer.append(world_cup[i+1])  # 우승자가 만난 연예인 기록
                    now_beautiful.append(how_beautiful[i])  # M의 매력점수 추가
                    now.append(M)  # 다음 진출조에 M 입력

                elif world_cup[i+1] == M:
                    answer.append(world_cup[i])
                    now_beautiful.append(how_beautiful[i+1])
                    now.append(M)

                else:  # 숫자끼리의 경우
                    if how_beautiful[i] == how_beautiful[i+1]:
                        now.append(min(world_cup[i], world_cup[i+1]))
                        now_beautiful.append(how_beautiful[i])
                    elif how_beautiful[i] > how_beautiful[i+1]:
                        now.append(world_cup[i])
                        now_beautiful.append(how_beautiful[i])
                    else:
                        now.append(world_cup[i+1])
                        now_beautiful.append(how_beautiful[i+1])

            else:
                now.append(world_cup[i])  # 부전승 처리
                now_beautiful.append(how_beautiful[i])  # 부전승 시 매력지수도 추가
        
        world_cup = now  # 나온 결과표를 다시 새로운 대진표로 형성
        how_beautiful = now_beautiful
    
    return answer
