Name = "AABAAABAA"


def solution(name):
    def min_updown(c):
        return min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

    N = len(name)
    answer = 0

    for char in name:
        answer += min_updown(char)

    move = N - 1

    for i in range(N):
        right = i + 1
        while right < N and name[right] == "A":
            right += 1

        dist = i + N - right + min(i, N - right)
        move = min(move, dist)

    answer += move
    return answer


print(solution(Name))

"""
내 코드가 틀린 이유 : A 최대 덩어리의 양 옆 기준으로만 확인했다.
모든 자리에서 왼쪽으로 돌지 오른쪽으로 돌지에 대한 값들을 확인했으면 좋았을 듯
A길이 상관없이 A 만나면 그걸 기준으로 생각하기 


def solution(name):
    def min_updown(c):
        return min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

    N = len(name)
    answer = 0
    
    for i in name:
        answer += min_updown(i)

    max_a_length = 0
    current_a_length = 0

    for char in name:
        if char == 'A':
            current_a_length += 1
            max_a_length = max(max_a_length, current_a_length)
        else:
            current_a_length = 0

    if max_a_length == 0:
        return answer + N - 1
    else:
        name = name.replace("A"*max_a_length, "*" * max_a_length)

        idx_left = 0
        idx_right = N-1
        left = 0
        right = 0
        while name[idx_left] != "*":
            left += 1
            idx_left += 1

        answer += left - 1

        while name[idx_right] != "*":
            right += 1
            idx_right -= 1

        answer += min(left - 1 + right, max_a_length + 1)
        return answer
"""
