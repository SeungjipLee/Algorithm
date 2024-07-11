# 어느 공원 놀이터에는 시소가 하나 설치되어 있습니다. 이 시소는 중심으로부터 2(m), 3(m), 4(m) 거리의 지점에 좌석이 하나씩 있습니다.
# 이 시소를 두 명이 마주 보고 탄다고 할 때, 시소가 평형인 상태에서 각각에 의해 시소에 걸리는 토크의 크기가 서로 상쇄되어 완전한 균형을 이룰 수 있다면 
# 그 두 사람을 시소 짝꿍이라고 합니다. 즉, 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍이라고 할 수 있습니다.
# 사람들의 몸무게 목록 weights이 주어질 때, 시소 짝꿍이 몇 쌍 존재하는지 구하여 return 하도록 solution 함수를 완성해주세요.


def solution(weights):
    answer = 0
    a = []

    for i in weights:
        line = []
        line = [i * 2, i * 3, i * 4]
        a.append(line)
        # 거리별로 숫자 계산해서
        # a라는 리스트에 넣기 [[]] 꼴

    for j in range(len(a)):
        for k in range(j+1, len(a)):
            if any(item in a[j] for item in a[k]):
                answer += 1

    return answer


# 시간초과 나서 다른 방법은

from collections import Counter
def solution(weights):
    answer = 0
    
    # 1:1
    counter = Counter(weights)
    for key,value in counter.items():
        if value>=2:
            answer+= value *(value-1)//2
            
    weights = set(weights) #1:1 구한 후 중복 제거  
    
    #2:3, 2:4, 3:4
    for w in weights:
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]
    return answer

# 라고 하는데... 솔직 밑에 식 이해가 안됨