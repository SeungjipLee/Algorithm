k = 2
d = 4


answer = 0

for i in range(0, d + 1, k):
    j = (d ** 2 - i ** 2)**(1/2)
    answer += int(j/k + 1)

print(answer)