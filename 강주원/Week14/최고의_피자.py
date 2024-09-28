import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
calories = sorted([int(input()) for _ in range(n)], reverse=True)
total_cost = a
total_calory = c
# 현재 칼로리 * 추가하려는 토핑 가격/(현재 가격 + 추가 하려는 토핑 가격) >
# 14000 * 2/(12+2) = 2000, 2000 이상의 칼로리만 가능 
for calory in calories:
    if total_calory * b / (total_cost + b) < calory:
        total_calory += calory
        total_cost += b
    else:
        break

print(int(total_calory/total_cost))