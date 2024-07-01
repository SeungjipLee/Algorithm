cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]

cards3 = ["i", "drink", "water"]

goal = ["i", "want", "to", "drink", "water"]
answer = "Yes"

for i in goal:
    if cards1 and i == cards1[0]:
        cards1.pop(0)
        continue

    if cards2 and i == cards2[0]:
        cards2.pop(0)
        continue

    answer = "No"
    break

print(answer)