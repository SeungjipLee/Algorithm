strings = ["sun", "bed", "car"]
n = 1

answer = []

for i in range(len(strings)):
    answer.append([strings[i][n], strings[i]])

answer.sort()

answer = [i[1] for i in answer]

print(answer)