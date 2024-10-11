def solution(arr1, arr2):
    n = len(arr1)
    answer = [[] for _ in range(n)]
    for idx, row1 in enumerate(arr1):
        
        for j in range(len(arr2[0])):
            tmp = 0
            for i, a in enumerate(row1):
                tmp += a * arr2[i][j]
            answer[idx].append(tmp)
    
    return answer