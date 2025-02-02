import sys
input = sys.stdin.readline

def main():
    # 용액의 개수 입력
    n = int(input().strip())
    # 용액 특성값 입력 후 정렬
    arr = list(map(int, input().split()))
    arr.sort()

    # 투 포인터 초기화
    left, right = 0, n - 1

    # 0에 가까운 합을 찾기 위한 변수
    best_sum = float('inf')
    answer = (0, 0)

    # 투 포인터 알고리즘
    while left < right:
        current_sum = arr[left] + arr[right]

        # 절대값이 더 작으면 갱신
        if abs(current_sum) < best_sum:
            best_sum = abs(current_sum)
            answer = (arr[left], arr[right])
        
        # 합이 0이면 완벽한 해를 찾은 것이므로 종료
        if current_sum == 0:
            break

        # 합이 음수면 left를 오른쪽으로, 양수면 right를 왼쪽으로 이동
        if current_sum < 0:
            left += 1
        else:
            right -= 1

    print(answer[0], answer[1])

if __name__ == '__main__':
    main()
