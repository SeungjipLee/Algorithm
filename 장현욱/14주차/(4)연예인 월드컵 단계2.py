# 연예인 월드컵을 진행할때, M번 연예인이 우승한다고 가정하고
# M번 연예인이 올라가면서 만나는 연예인들의 번호를 모두 구하시오
# M번 연예인 외의 인물은 선호하는 매력이 있는 연예인이, 둘다 있거나 없을 경우 매력점수가 더 높은 연예인이, 같을 경우 아이디가 더 적은 선수가 올라갑니다.
# N = [대회 참가한 연예인 번호]
# M = 우승자 번호
# A = [매력점수]
# E = [매력의 종류]
# P = 내가 선호하는 매력

def solution(N, M, A, E, P):
    answer = []
    world_cup = list(range(1, N+1))  # 연예인들 아이디 정렬 [1, 2, 3, ...]
    
    # 매력지수는 그대로 사용
    how_beautiful = A[:]
    
    # 매력의 종류는 E의 2차원 배열을 그대로 사용
    kind_beautiful = E[:]
    
    # 월드컵 진행
    while len(world_cup) > 1:
        now = []  # 이번 대진의 결과
        now_beautiful = []
        now_kind = []
        
        for i in range(0, len(world_cup), 2):  # 두 명씩 비교하므로 두 칸씩
            if i + 1 < len(world_cup):  # 마지막 번호의 짝이 있을 때만 비교
                if world_cup[i] == M:  # 우승자 M이 있다면
                    answer.append(world_cup[i+1])  # M이 만난 연예인 기록
                    now_beautiful.append(how_beautiful[i])  # M의 매력 점수 추가
                    now_kind.append(kind_beautiful[i])  # M의 매력 종류 추가
                    now.append(M)  # M은 다음 라운드로 진출

                elif world_cup[i+1] == M:
                    answer.append(world_cup[i])
                    now_beautiful.append(how_beautiful[i+1])
                    now_kind.append(kind_beautiful[i+1])
                    now.append(M)

                else:  # M이 없는 경우 매력 비교
                    # 둘 다 선호하는 매력을 가지고 있을 경우
                    if P in kind_beautiful[i] and P in kind_beautiful[i+1]:
                        if how_beautiful[i] == how_beautiful[i+1]:  # 매력 지수가 같다면
                            now.append(min(world_cup[i], world_cup[i+1]))
                            now_beautiful.append(how_beautiful[i])
                            now_kind.append(kind_beautiful[i])
                        elif how_beautiful[i] > how_beautiful[i+1]:  # 첫 번째가 더 매력적이라면
                            now.append(world_cup[i])
                            now_beautiful.append(how_beautiful[i])
                            now_kind.append(kind_beautiful[i])
                        else:  # 두 번째가 더 매력적이라면
                            now.append(world_cup[i+1])
                            now_beautiful.append(how_beautiful[i+1])
                            now_kind.append(kind_beautiful[i+1])
                    
                    # 한 명만 선호하는 매력을 가진 경우
                    elif P in kind_beautiful[i]:
                        now.append(world_cup[i])
                        now_beautiful.append(how_beautiful[i])
                        now_kind.append(kind_beautiful[i])
                    
                    elif P in kind_beautiful[i+1]:
                        now.append(world_cup[i+1])
                        now_beautiful.append(how_beautiful[i+1])
                        now_kind.append(kind_beautiful[i+1])
                    
                    # 둘 다 선호하는 매력이 없을 경우
                    else:
                        if how_beautiful[i] == how_beautiful[i+1]:  # 매력 지수가 같다면
                            now.append(min(world_cup[i], world_cup[i+1]))
                            now_beautiful.append(how_beautiful[i])
                            now_kind.append(kind_beautiful[i])
                        elif how_beautiful[i] > how_beautiful[i+1]:  # 첫 번째가 더 매력적이라면
                            now.append(world_cup[i])
                            now_beautiful.append(how_beautiful[i])
                            now_kind.append(kind_beautiful[i])
                        else:  # 두 번째가 더 매력적이라면
                            now.append(world_cup[i+1])
                            now_beautiful.append(how_beautiful[i+1])
                            now_kind.append(kind_beautiful[i+1])

            else:  # 대진 상대가 없을 경우 부전승 처리
                now.append(world_cup[i])
                now_beautiful.append(how_beautiful[i])
                now_kind.append(kind_beautiful[i])

        # 다음 라운드로 넘어가면서 리스트 갱신
        world_cup = now
        how_beautiful = now_beautiful
        kind_beautiful = now_kind
        
    return answer