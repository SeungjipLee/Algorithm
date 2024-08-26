from collections import deque

order = [4, 3, 1, 2, 5]


def solution(order):
    order = deque(order)  # 트럭에 실어야 하는 순서
    belt = deque(range(1, len(order) + 1))  # 1부터 n까지의 상자
    stack = []  # 보조 컨베이어 벨트 역할

    answer = 0

    while order:
        now = order[0]

        if belt and belt[0] == now:
            # 벨트에서 바로 트럭으로 상자를 싣는 경우
            belt.popleft()
            order.popleft()
            answer += 1
        elif stack and stack[-1] == now:
            # 보조 컨베이어 벨트에서 트럭으로 상자를 싣는 경우
            stack.pop()
            order.popleft()
            answer += 1
        elif belt:
            # 현재 벨트에서 상자를 보조 컨베이어 벨트로 옮기는 경우
            stack.append(belt.popleft())
        else:
            # 더 이상 처리할 수 없는 경우 종료
            break

    return answer


print(solution(order))
