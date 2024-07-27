food = [1, 3, 4, 6]

answer = ""
half = ""

counting = [0] * len(food)

for i in range(1, len(food)):
    counting[i] = food[i] // 2

for j in range(1, len(counting)):
    half += str(j) * counting[j]

answer = half + "0" + half[::-1]

print(answer)