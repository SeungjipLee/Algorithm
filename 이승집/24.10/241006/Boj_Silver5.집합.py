import sys

S = 0  # 비트마스크를 위한 변수
M = int(sys.stdin.readline())

for _ in range(M):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'add':
        S |= (1 << (int(cmd[1]) - 1))
    elif cmd[0] == 'remove':
        S &= ~(1 << (int(cmd[1]) - 1))
    elif cmd[0] == 'check':
        if S & (1 << (int(cmd[1]) - 1)):
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif cmd[0] == 'toggle':
        S ^= (1 << (int(cmd[1]) - 1))
    elif cmd[0] == 'all':
        S = (1 << 20) - 1
    elif cmd[0] == 'empty':
        S = 0


"""
🔹 예제를 통해 단계별로 설명:

초기 상태:

프로그램 시작 시, S = 0입니다. 이는 모든 비트가 0인 상태로, 빈 집합을 의미합니다.
1. 명령어 add 3 실행:

현재 S = 0b00000000000000000000 (20개의 비트, 모두 0)

비트 마스크 생성:

1 << (3 - 1) → 1 << 2 → 0b00000000000000000100
S에 원소 3 추가:

S |= 0b00000000000000000100
연산 결과: 0b00000000000000000000 | 0b00000000000000000100 → 0b00000000000000000100
새로운 S의 값은 0b00000000000000000100, 즉 원소 3만 포함
2. 명령어 add 5 실행:

현재 S = 0b00000000000000000100

비트 마스크 생성:

1 << (5 - 1) → 1 << 4 → 0b00000000000000010000
S에 원소 5 추가:

S |= 0b00000000000000010000
연산 결과: 0b00000000000000000100 | 0b00000000000000010000 → 0b00000000000000010100
새로운 S의 값은 0b00000000000000010100, 원소 3과 5를 포함
3. 명령어 remove 3 실행:

현재 S = 0b00000000000000010100

비트 마스크 생성:

1 << (3 - 1) → 1 << 2 → 0b00000000000000000100
반전 비트 마스크: ~(1 << (3 - 1)) → ~0b00000000000000000100 → 0b11111111111111111011
S에서 원소 3 제거:

S &= 0b11111111111111111011
연산 결과: 0b00000000000000010100 & 0b11111111111111111011 → 0b00000000000000010000
새로운 S의 값은 0b00000000000000010000, 원소 5만 포함
4. 명령어 check 5 실행:

현재 S = 0b00000000000000010000

비트 마스크 생성:

1 << (5 - 1) → 1 << 4 → 0b00000000000000010000
S에 원소 5가 있는지 확인:

S & 0b00000000000000010000
연산 결과: 0b00000000000000010000 & 0b00000000000000010000 → 0b00000000000000010000 (0이 아니므로 존재)
출력: 1
5. 명령어 toggle 5 실행:

현재 S = 0b00000000000000010000

비트 마스크 생성:

1 << (5 - 1) → 1 << 4 → 0b00000000000000010000
S에서 원소 5를 반전:

S ^= 0b00000000000000010000
연산 결과: 0b00000000000000010000 ^ 0b00000000000000010000 → 0b00000000000000000000
새로운 S의 값은 0b00000000000000000000, 빈 집합
6. 명령어 all 실행:

모든 비트를 1로 설정:
S = (1 << 20) - 1
계산: (1 << 20)은 0b100000000000000000000 (21비트, 비트 20이 1)
(1 << 20) - 1 → 0b11111111111111111111 (20개의 비트, 모두 1)
새로운 S의 값은 0b11111111111111111111, 원소 1부터 20까지 모두 포함
7. 명령어 empty 실행:

S를 0으로 설정:
S = 0
새로운 S의 값은 0b00000000000000000000, 빈 집합
"""