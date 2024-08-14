# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 
# 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
# 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

# .remove(원하는 값)
# del 리스트이름[인덱스] => 해당인덱스 값 삭제
# .pop(인덱스번호) => 해당 인덱스 번호 값 삭제

# n = 전체 학생수 5
# lost = 잃어버린 학생 2, 4 
# reserve = 여분이 있는 학생번호 1 3 5
import copy
def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    next_lost = copy.deepcopy(lost)
    for i in lost:
        if i in reserve: # i의 -1 ~ +1 사이에 값이 있다면  
            next_lost.remove(i)
            reserve.remove(i)  # 해당 값을 지우기
    
    for j in next_lost:
        if j-1 in reserve:
            reserve.remove(j-1)
        elif j+1 in reserve:
            reserve.remove(j+1)
        else:
            answer -= 1

    return answer

print(solution(5, [2, 3, 5], [2, 3, 4]))