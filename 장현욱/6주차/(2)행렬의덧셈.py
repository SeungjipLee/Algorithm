def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        now = []
        for j in range(len(arr1[0])):
            now.append(arr1[i][j] + arr2[i][j])
        answer.append(now)
    return answer