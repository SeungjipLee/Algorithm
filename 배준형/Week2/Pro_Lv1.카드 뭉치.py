def solution(cards1, cards2, goal):
    answer = ''
    len1 = len(cards1)
    len2 = len(cards2)    
    card1 = 0
    card2 = 0
    goal_idx = 0
    
    while True:
        if goal_idx == len(goal):
            break
        if card1 < len1 and cards1[card1] == goal[goal_idx]:
            card1 += 1
        elif card2 < len2 and cards2[card2] == goal[goal_idx]:
            card2 += 1
        else:
            answer = "No"
            return answer
        goal_idx += 1
    
    answer = "Yes"
    return answer