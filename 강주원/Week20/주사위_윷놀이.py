# dice = list(map(int, input().split()))
# '''
# 22, 24, 26, 28, 30은 2개씩 있음
# '''
# road = {0: [2,4,6,8,10], 2: [4,6,8,10,12], 4: [6,8,10,12,14], 6: [8,10,12,14,16], 8: [10,12,14,16,18], 10: [13,16,19,25,30], }
# a = {22: [24,25,30,35,40], 24: [25, 30, 35, 40, -0]}
# '''
# 고득점하려면 파란 영역으로 가야함
# 근데 꼭 그럴까?
# 5 4 4 1 1 1 1 1 1 1 1 1 1 1 1 1
# 이 경우 파란영역을 우선으로 좇으면 5 4 4로 끝난다
# 그러나 1 1 1 1 1 1 1 1 1 1 1 1 1
# 이렇게 가면 훨씬 많은 점수 획득 가능
# 그럼 완탐을 하는게 좋아 bfs 혹은 dfs

# 주사위는 1~5이고 각 숫자의 개수를 센다
# {1: 3, 2: 3, 3: 2, 4: 2, 5: 0}
# now = []
# def back(now):
#     그냥 dice[0]으로 가서 새로 시작하거나, 기존의 말을 dice[0]만큼 이동하는 방법이 있다
#     for i in dice:
#         if now
        

    

# back(now)
        
# 예제 1
# 2+4+10+25+4+35+10+25+40+35
# now = [1, 2, 3, 4]
# '''
# my_dict = {i:0 for i in range(1, 6)}
# for i in dice:
#     my_dict[i] += 1

# res = 0
# def back(dice_order, total, now, dir, depth):
#     if depth == len(dice):
#         res = max(res, )
#         return
    
#     for i in range(1, 6):
#         if dice_order[i]:
#             temp = dice_order.copy()
#             temp[i] -= 1
#             back(temp, total + board[now], now+a, road[i], depth+1)
res = []
res.append(-0)
print(res)