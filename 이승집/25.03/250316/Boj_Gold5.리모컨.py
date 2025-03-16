import sys


def is_possible(channel, broken):
    for digit in str(channel):
        if digit in broken:
            return False
    return True


def min_press(N, broken):
    min_count = abs(N - 100)  # +, - 버튼만 사용
    for channel in range(1000000):  # 모든 경우 탐색 (0 ~ 999999)
        if is_possible(channel, broken):
            press_count = len(str(channel)) + abs(channel - N)
            min_count = min(min_count, press_count)

    return min_count


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    broken = set(sys.stdin.readline().split()) if M > 0 else set()

    print(min_press(N, broken))
