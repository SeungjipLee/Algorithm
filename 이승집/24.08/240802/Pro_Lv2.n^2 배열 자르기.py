n = 3
left = 2
right = 5

"""
n이 3인 경우

1 2 3
2 2 3
3 3 3

으로 배치가 되고
이를 1차열로 푼다면


1 2 [3 2 2 3] 3 3 3 3 이 된다.
이를 2번부터 5번 idx 까지 자르면 [ ] 사이가 된다.





1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5
"""

Board = [list(range(1, n + 1)) for _ in range(n)]

print(Board)


for i in range(n):
    for j in range(n):
        Board[i][j] = max(i, j) + 1

answer = []
for i in Board:
    answer += i
print(answer[left: right + 1])


"""
def solution(n, left, right):
    answer = []
    for idx in range(left, right + 1):
        i = idx // n
        j = idx % n
        answer.append(max(i, j) + 1)
    
    return answer
    
-> 시간 초과 해결 풀이(Board를 만들지 않기)
"""