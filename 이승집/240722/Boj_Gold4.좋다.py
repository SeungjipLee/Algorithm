N = int(input())
num_list = list(map(int, input().split()))

cnt = 0

num_list.sort()

for i in range(N):
    target = num_list[i]
    found = False

    for j in range(N):
        if j == i:
            continue
        for k in range(j + 1, N):
            if k == i:
                continue
            if num_list[j] + num_list[k] == target:
                found = True
                break
        if found:
            break

    if found:
        cnt += 1

print(cnt)