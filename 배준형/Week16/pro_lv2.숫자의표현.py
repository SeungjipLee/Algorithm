def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if i % 2:
            if n % i == 0 and n//i > i//2:
                # print(i)
                answer += 1
        else:
            if n % i == i // 2 and n//i >= i//2:
                # print(i)
                answer += 1
    
    return answer