numbers = [2, 7]
answer = []

for i in numbers:
    A = bin(i)[2:]
    mid = 0
    while True:
        i += 1
        B = bin(i)[2:]
        cnt = 0
        M = max(len(A), len(B))
        A, B = A.zfill(M), B.zfill(M)

        for j in range(M):
            if A[j] != B[j]:
                cnt += 1
            if cnt > 2:
                break
        if cnt <= 2:
            mid = int(B, 2)
            break
    answer.append(mid)

print(answer)

"""
시간 초과가 남 -> 규칙 찾기

1. 짝수면 0으로 끝나기 때문에 마지막만 1로 바꾸면 됨 -> 1만 증가한 수
2. 전부 1로 되어있다면 자리수가 바뀐다. -> 맨 앞을 10하고 뒤를 전부 1로 두면 된다.
3. 아닌 경우는 끝의 01 을 10으로만 바꿔주면 최소한으로 바꾸고 2개만 변하게 됨
"""


def solution(nums):
    ans = []
    for num in nums:
        if num % 2 == 0:
            ans.append(num + 1)
        else:
            bit_string = bin(num)[2:]
            if '0' not in bit_string:
                # 모든 비트가 1인 경우: '111' -> '1011'
                bit_string = '10' + bit_string[1:]
            else:
                # 가장 우측의 '01'을 '10'으로 변경
                bit_string = bit_string[::-1].replace('10', '01', 1)[::-1]
            ans.append(int(bit_string, 2))
    return ans


print(solution(numbers))
