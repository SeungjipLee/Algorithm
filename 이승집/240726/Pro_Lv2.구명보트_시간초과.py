people = [70, 50, 80, 50]
limit = 100

people.sort(reverse=True)
print(people)
visited = [-1] * len(people)
answer = []
for i in range(len(people)):
    if visited[i] == 1:
        continue
    mid = [people[i]]
    for j in range(len(people)-1, 0, -1):
        if visited[j] == -1 and sum(mid) + people[j] <= limit:
            mid += [people[j]]
            visited[j] = 1
            break
    answer.append(mid)
print(answer)
