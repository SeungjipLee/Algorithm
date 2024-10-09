# n개의 음이 아닌 정수들이 있습니다. 
# 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 
# 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 
# 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.


# 오답 시간초과
import itertools
def solution(numbers, target):
    answer = 0
    # 크기순으로 정렬을 한번 하고 [+,-]
    numbers.sort(reverse=True)  # 크기가 큰것부터 정렬
    number = [] # +가 몇개 필요한지 찾을때 쓸 리스트
    find_number = []  # 마지막 계산을 할 때 사용할 리스트
    # 최소한의 + 갯수
    plus = 0
    # +,- 리스트
    susick = [-1 for _ in range(len(numbers))]  # 수식 저장리스트
    for i in numbers:
        number.append(-i)  # 음수로 전환
        find_number.append(-i)

    for j in range(len(number)):
        number[j] = number[j] * -1  # 양수로 변경
        if sum(number) >= target:  # 총 합이 타겟보다 크면 통과
            plus = j+1  # 최소 필요한 +의 갯수
            break
    for k in range(len(susick)):
        if k < plus:
            susick[k] = 1
        else:
            result = [list(item) for item in set(itertools.permutations(susick, len(susick)))]
            for now_result in result:
                result_list = []
                for l in range(len(now_result)):
                    result_list.append(numbers[l] * now_result[l])
                if sum(result_list) == target:
                    answer += 1
            susick[k] = 1
    
    return answer


# BFS넓게 탐색
def solution(numbers, target):
    answer = 0  
    leaves = [0]  # 계산 결과 담는곳
    for num in numbers:  # 숫자 하나씩 넣기
        tmp = []  # 지금의 결과값
        # 자손노드
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp  # 결과값을 쌓아가기
        print(leaves)

    for leaf in leaves:
        if leaf == target:  # 타겟과 일치하면
            answer += 1  # 카운트 올리기
    return answer

# # DFS 깊게 탐색
# def dfs(numbers, target, idx, values):     # idx : 깊이 / values : 더하고 뺄 특정 leaf 값 
	
#     global cnt
#     cnt = 0 
	
#     # 깊이가 끝까지 닿았으면 
#     if idx == len(numbers) & values == target : 
#     	cnt += 1
#         return 
  
#     # 끝까지 탐색했는데 sum이 target과 다르다면 그냥 넘어간다
#     elif idx == len(numbers) : 
#     	return 
    
#     # 재귀함수로 구현 
#     dfs(numbers, target, idx+1, values + numbers[idx])   # 새로운 value 값 세팅   
#     dfs(numbers, target, idx+1, values - numbers[idx])
 
#  def solution(numbers, target) : 
 	
#     global cnt
#     dfs(numbers, target, 0, 0)
    
#     return cnt