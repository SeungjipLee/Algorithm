n, k = map(int, input().split())
quests = sorted(list(map(int, input().split())))

sum_val = sum(quests)
Exp = 0
for i in range(k):
    sum_val -= quests[i]
    Exp += sum_val

print(Exp)