from math import gcd

# arrayA = [10, 17]
# arrayB = [5, 20]
# arrayA = [10, 20]
# arrayB = [5, 17]
arrayA = [14, 35, 119]
arrayB = [18, 30, 102]

GA = gcd(*arrayA)
GB = gcd(*arrayB)

print(GA, GB)
answer = 0

for i in arrayA:
    if i % GB == 0:
        break
else:
    answer = max(GB, answer)

for j in arrayB:
    if j % GA == 0:
        break
else:
    answer = max(GA, answer)

print(answer)