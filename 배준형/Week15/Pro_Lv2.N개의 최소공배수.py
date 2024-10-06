from collections import defaultdict
import math

def solution(arr):
    answer = 1
    
    prime_nums = make_prime_num()
    primes = {i : 0 for i in prime_nums}
    # print(primes)
    
    for num in arr:
        divs = get_divisor(num, prime_nums)
        for pn in divs:
            if primes[pn] <= divs[pn]:
                primes[pn] = divs[pn]
    
    for num in primes:
        answer *= num ** primes[num]
    
    return answer

def get_divisor(num, prime_nums):
    divisors = defaultdict(int)
    for prime_num in prime_nums:
        while num % prime_num == 0:
            divisors[prime_num] += 1
            num //= prime_num
    return divisors

def make_prime_num():
    not_primes = {}
    primes = []
    for i in range(2, 101):
        if not_primes.get(i) != None:
            continue
        primes.append(i)
        j = 2
        while i * j <= 100:
            not_primes[i*j] = True
            j += 1
    
    return primes