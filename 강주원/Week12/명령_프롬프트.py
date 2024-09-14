n = int(input())
strings = [input().strip() for _ in range(n)]

result = list(strings[0])

for j in range(len(result)):
    char = result[j]
    for i in range(1, n):
        if strings[i][j] != char:
            result[j] = '?'
            break

print(''.join(result))
