from collections import defaultdict
memo = defaultdict(dict)

def solution(n):
    answer = 0
    for i in range(n//2+1):
        if i == 0:
            answer += 1
            continue

        a = n - i
        b = i
        if memo.get(a) != None and memo[a].get(b) != None:
            answer += memo[a][b]
        else:
            result = factorial(a, b)
            answer += result
            memo[a][b] = result
        answer %= 1_000_000_007     

    return answer

def factorial(n, r):
    tmp = 1
    num = 1
    for i in range(n, n-r, -1):
        tmp *= i
        tmp //= num
        num += 1
    return tmp