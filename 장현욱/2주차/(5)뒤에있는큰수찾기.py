# 정수로 이루어진 배열 numbers가 있습니다. 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
# 정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        if i < len(numbers)-1:
          for j in range(i+1, len(numbers)):
              if numbers[i] < numbers[j]:
                  answer.append(numbers[j])
                  break
              elif j == len(numbers)-1:
                  answer.append(-1)
                  break
        else:
            answer.append(-1)
    return answer


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
            # 넘버의[스택의 오른쪽번호] = number[i]가 됨 즉 큰 수로 교체됨
        stack.append(i)
        # 스택은 아직 큰 수를 찾지못한 숫자를 넣어놓는곳

    return answer


stack = 0