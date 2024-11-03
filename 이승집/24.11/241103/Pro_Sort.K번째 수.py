def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        mid = array[i-1:j]
        mid.sort()
        answer.append(mid[k-1])
    return answer