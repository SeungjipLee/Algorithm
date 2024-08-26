skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
answer = 0

for i in skill_trees:
    mid = ""
    for j in i:
        if j in skill:
            mid += j
    if skill[:len(mid)] == mid:
        answer += 1

print(answer)