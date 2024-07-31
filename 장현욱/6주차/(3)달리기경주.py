# 얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
# 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 
# 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

# 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 
# 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

def solution(players, callings):
    answer = []
    for i in range(len(callings)):
        for j in range(len(players)):
            if players[j] == callings[i]:
                players[j], players[j-1] = players[j-1], players[j]
    answer = players
    return answer


# 1차 개선
def solution(players, callings):
    answer = []
    for i in callings:
        now_index = players.index(i)
        players[now_index], players[now_index - 1] = players[now_index - 1], players[now_index]
    return players

# 해결 문항
def solution(players, callings):
    # 이름별 정렬
    player_name = {player: i for i, player in enumerate(players)}
    # 순위별 정렬
    player_rank = {i: player for i, player in enumerate(players)}
    
    for call in callings:
        now_rank = player_name[call] # 이름 부른 사람 순위
        front_rank = now_rank - 1
        front_name = player_rank[front_rank] # 앞사람의 이름
        
        player_name[call] = front_rank # 부른사람은 앞으로
        player_name[front_name] = now_rank # 앞사람은 뒤로
        player_rank[front_rank] = call # 앞의 랭크로 이름 부른 사람 올리기
        player_rank[now_rank] = front_name # 뒤의 랭크에 앞에있던 사람 이름 내리기
        
    
    answer = [player_rank[key] for key in player_rank.keys()] 
    # player_rank의 키 값을 가지고 ex[0,1,2,3] 정렬을 원하면 sorted사용 반복문을 돌림 player_rank[키값] 즉 해당 키의 밸류를 정답에 넣어서 리스트 완성
    
    return answer