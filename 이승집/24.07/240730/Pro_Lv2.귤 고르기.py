from collections import Counter

k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
answer = 0
print(Counter(tangerine))
A = Counter(tangerine).most_common()
"""
Counter는 많은 것 순으로 제공해준다
"""

for i in A:
    if k > 0:
        k -= i[1]
        answer += 1
    else:
        break

print(answer)
