def solution(n):
    answer = []
    hanoi(n, 1, 3, answer)
    return answer

def hanoi(top, s, e, answer):
    if top == 1:
        answer.append([s, e])
        return
    # n-1 top move
    hanoi(top-1, s, 6-s-e, answer)
    # n plate move
    answer.append([s, e])
    # n top complete
    hanoi(top-1, 6-s-e, e, answer)
        