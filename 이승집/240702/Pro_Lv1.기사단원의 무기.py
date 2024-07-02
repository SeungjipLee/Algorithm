def counting(n):
    if n == 1:
        return 1

    cnt = 2
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            cnt += 2
            if i ** 2 == n:
                cnt -= 1
    return cnt


def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        answer += counting(i) if counting(i) <= limit else power

    return answer