name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
value = dict()
answer = []

for i in range(len(name)):
    value[name[i]] = yearning[i]

for i in photo:
    mid = 0
    for j in i:
        mid += value[j] if j in value else 0
    answer.append(mid)

print(answer)