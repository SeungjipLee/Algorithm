import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 설정 (n이 클 때 대비)


def hanoi(n, start, auxiliary, end, moves):
    if n == 1:
        moves.append(f"{start} {end}")
        return

    # 1. n-1개 원판을 보조 기둥으로 옮김
    hanoi(n - 1, start, end, auxiliary, moves)

    # 2. 가장 큰 원판을 목표 기둥으로 옮김
    moves.append(f"{start} {end}")

    # 3. 보조 기둥의 n-1개 원판을 목표 기둥으로 옮김
    hanoi(n - 1, auxiliary, start, end, moves)


# 입력 받기
n = int(sys.stdin.readline())
moves = []

# 하노이의 탑 이동 수행
hanoi(n, 1, 2, 3, moves)

# 결과 출력
print(len(moves))  # 이동 횟수 출력
print('\n'.join(moves))  # 이동 경로 출력
