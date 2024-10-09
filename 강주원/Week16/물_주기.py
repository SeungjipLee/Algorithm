n, k, a, b = map(int, input().split())

d = n/a
data = []
count = 0
check = 0

for _ in range(int(d)):
    data.append(k)
while True:
    for i in range(int(d)):
        data[i] -= 1

    data[check] += b
    check += 1
    if check == int(d):
        check = 0
    count += 1
    if min(data) == 0:
        print(count)
        break