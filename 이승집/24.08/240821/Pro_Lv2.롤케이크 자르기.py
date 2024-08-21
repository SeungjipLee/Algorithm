from collections import Counter

topping = [1, 2, 1, 3, 1, 4, 1, 2]
answer = 0
Cnt = Counter(topping)
print(Cnt)
A = set()
for i in topping:
    Cnt[i] -= 1
    if Cnt[i] == 0:
        del Cnt[i]
    A.add(i)
    if len(A) == len(Cnt):
        answer += 1
print(answer)