N = int(input())
arr = list(map(int, input().split()))

tails = []

for num in arr:
    # 비어있다면 넣기
    if not tails:
        tails.append(num)
        continue
    
    # 값이 가장 크다면 추가
    if num > tails[-1]:
        tails.append(num)
        continue

    # 값이 중간 값이라면 그 값을 대체 (이분 탐색)
    start, end = 0, len(tails) - 1
    while start < end:
        mid = (start + end) // 2
        if num <= tails[mid]:
            end = mid  # num이 작거나 같으면 왼쪽으로 탐색
        else:
            start = mid + 1  # num이 크면 오른쪽으로 탐색
    
    tails[start] = num  # 이분 탐색 후 찾은 위치에 값 대체

# 최종 LIS 길이 출력
print(len(tails))
