import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
calories = sorted([int(input()) for _ in range(n)], reverse=True)
total_cost = a
total_calory = c

for calory in calories:
    if total_calory * b / (total_cost + b) < calory:
        total_calory += calory
        total_cost += b
    else:
        break

print(int(total_calory/total_cost))