def solution(n):
    answer = 0
    x = count_1(bin(n))

    while True:
        n += 1
        if x == count_1(bin(n)):
            break
    
    return n
    
def count_1(bin_num):
    cnt = 0
    for i in bin_num:
        if i == "1":
            cnt += 1
    return cnt