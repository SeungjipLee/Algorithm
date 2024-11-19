def solution(number, k):
    answer = ''
    for _ in range(k):
        i = 0
        j = 1
        deleted = False
        while True:
            if j >= len(number):
                break
            if number[i] < number[j]:
                number = number[0:i] + number[j:]
                deleted = True
                break
            i += 1
            j += 1
        if not deleted:
            number = number[:-1]
            
    return number