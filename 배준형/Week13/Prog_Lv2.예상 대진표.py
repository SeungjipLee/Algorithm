def solution(n,a,b):
    answer = 0
    size =  2 ** (n-1).bit_length()
    a += size-1
    b += size-1
    
    while a != b:
        answer += 1
        a //= 2
        b //= 2
        

    return answer