def solution(triangle):
    answer = 0
    
    len_t = len(triangle)

    for i in range(1, len_t):
        for j in range(i+1):
            if j-1 < 0:
                triangle[i][j] += triangle[i-1][j]
                continue
            if j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    answer = max(triangle[len_t-1])
        
    return answer