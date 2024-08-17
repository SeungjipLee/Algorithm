"""
1. 소수 구하는 함수 만들기 -> 에라토스테네스의 체
2. 0을 기준으로 카운팅
3. 각 요소가 소수인지 확인
"""


def check_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    for i in range(2, int(n ** (1 / 2)) + 2):
        if n % i == 0:
            return False
    return True


n = 437674
k = 3
answer = 0
mid = ""
while n >= k:
    mid = str(n%k) + mid
    n //= k
mid = str(n) + mid
mid2 = ''

print(mid)

for i in mid:
    if i == '0' :
        if mid2 != '' and check_prime(int(mid2)):
            answer += 1
        mid2 = ''
    else:
        mid2 += i

if mid2 and check_prime(int(mid2)):
    answer += 1

print(answer)