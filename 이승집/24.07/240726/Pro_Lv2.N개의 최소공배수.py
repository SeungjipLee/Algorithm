from math import lcm

arr = [2,6,8,14]
answer = arr[0]

for i in arr:
    answer = lcm(answer, i)

print(answer)