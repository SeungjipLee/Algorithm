from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    n = len(want)
    m = len(discount)
    k = sum(number)
    wants = {}
    discounts = defaultdict(int)
    for i in range(n):
        wants[want[i]] = number[i]
    
    for j in range(m):
        discounts[discount[j]] += 1
        if j >= 10:
            discounts[discount[j-10]] -= 1
        if j >= 9:
            if is_valid(wants, discounts):
                answer += 1
        
    return answer
    

def is_valid(wants, discounts):
    for want in wants:
        if wants[want] <= discounts[want]:
            continue
        else:
            return False
    return True