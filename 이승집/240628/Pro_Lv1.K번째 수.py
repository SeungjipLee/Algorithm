def solution(array, commands):
    answer = []
    for command in commands:
        mid = array[command[0]-1:command[1]]
        mid.sort()
        answer.append(mid[command[2]-1])
    return answer
