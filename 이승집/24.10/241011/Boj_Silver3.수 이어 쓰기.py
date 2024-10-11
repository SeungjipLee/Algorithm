N = "1111111111111"
target_idx = 0
num = 1

while target_idx < len(N):
    str_num = str(num)

    for digit in str_num:
        if target_idx < len(N) and digit == N[target_idx]:
            target_idx += 1

    num += 1

print(num - 1)