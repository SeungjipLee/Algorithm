def dfs(idx, current_result, add, sub, mul, div):
    global max_result, min_result

    # 모든 숫자를 사용했으면 결과 갱신
    if idx == n:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    # 각 연산자별로 남은 개수가 있으면 사용
    if add > 0:
        dfs(idx + 1, current_result + numbers[idx], add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, current_result - numbers[idx], add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, current_result * numbers[idx], add, sub, mul - 1, div)
    if div > 0:
        # 음수를 양수로 나눌 때 주의: 문제에서 정수 나눗셈 규칙 따름
        if current_result < 0:
            dfs(idx + 1, -(-current_result // numbers[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, current_result // numbers[idx], add, sub, mul, div - 1)

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 결과 초기화
max_result = -float('inf')
min_result = float('inf')

# DFS 시작
dfs(1, numbers[0], add, sub, mul, div)

# 최댓값과 최솟값 출력
print(max_result)
print(min_result)
