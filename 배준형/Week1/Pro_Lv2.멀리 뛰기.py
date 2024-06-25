factorial = [0] * 2001
factorial[1] = 1
for i in range(2, 2001):
    factorial[i] = i * factorial[i-1]
    
def solution(n):
    k = n // 2
    answer = 1
    
    for i in range(1, k+1):
        a = n - i
        if a-i == 0:
            answer += 1
        else:
            answer += factorial[a]//factorial[i]//factorial[a-i] % 1234567
        
    return answer % 1234567