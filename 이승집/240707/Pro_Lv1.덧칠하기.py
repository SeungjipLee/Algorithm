# 전체 길이 1 ~ n까지
n = 8
# 페인트 붓 길이 m칸
m = 4
# 빵꾸난 부분
section = [2, 3, 6]
# 결과
result = 0

# 전체를 색칠된 부분
colored = [True] * (n + 1)

# 색칠하기
for i in section:
    colored[i] = False

# 빈 부분 색칠하기
for i in range(1, n + 1):
    if not colored[i]:
        for j in range(m):
            if i + j <= n and not colored[i + j]:
                colored[i + j] = True
        result += 1

print(result)