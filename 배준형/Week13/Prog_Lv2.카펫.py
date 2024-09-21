def solution(brown, yellow):
    answer = []
    
    area = brown + yellow
    
    for i in range(3, area//3+1):
        if area % i:
            continue
        j = area // i
        if (i + j) * 2 == brown + 4:
            break
    
    return [max(i, j), min(i, j)]