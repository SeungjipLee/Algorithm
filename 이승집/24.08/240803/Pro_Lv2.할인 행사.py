want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

answer = 0
whole_cnt = sum(number)
l = len(want)

# want_dict = {want[i]: number[i] for i in range(len(want))}
# print(want_dict)

compare = []
for i in range(l):
    compare += [want[i]] * number[i]

compare.sort()

for i in range(len(discount)-9):
    A = discount[i:i+10]
    A.sort()
    if A == compare:
        answer += 1

print(answer)