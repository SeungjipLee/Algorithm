def solution(numbers):
    answer = ''
    # 천의 자리, 백의 자리, 십의 자리, 일의 자리
    numbers.sort(key=lambda x: (-num_head(x, 3), -num_head(x, 2), -num_head(x, 1), -num_head(x, 0), -x))
    # print(numbers)
    for num in numbers:
        answer += str(num) 
    
    return str(int(answer))
                 
def num_head(num, n):
    if num < 10:
        # print(num, n)
        return num
    elif num >= 1000:
        pass
    elif num >= 100:
        a = num // 100
        num *= 10
        num += a
    elif num >= 10:
        a = num
        num *= 100
        num += a
    if n == 2:
        num %= 1000
    elif n == 1:
        num %= 100
    elif n == 0:
        num %= 10
    # print(num, n, num//(10**n))
    return num // (10**n)
