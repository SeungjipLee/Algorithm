people = [70, 50, 80, 50]
limit = 100

left, right = 0, len(people) - 1
answer = 0
people.sort()

while left < right:
    if people[left] + people[right] <= limit:
        left += 1
        right -= 1
        answer += 1
    else:
        right -= 1
        answer += 1

print(answer)