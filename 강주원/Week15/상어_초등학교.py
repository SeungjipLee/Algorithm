import sys
input = sys.stdin.readline

n = int(input())
classroom = [[0]*n for _ in range(n)]
like_students = [[] for _ in range(n**2+1)]

for _ in range(n**2):
    student_num, like_1, like_2, like_3, like_4 = map(int, input().split())
    like_students[student_num].append((like_1, like_2, like_3, like_4))

    max_like = -1
    max_blank = -1
    best_seat = (-1, -1)

    for i in range(n):
        for j in range(n):
            if classroom[i][j] != 0:
                continue

            like = 0
            blank = 0

            for d in [(1,0), (0,1), (-1,0), (0,-1)]:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < n and 0 <= nj < n:
                    if classroom[ni][nj] in (like_1, like_2, like_3, like_4):
                        like += 1
                    
                    elif classroom[ni][nj] == 0:
                        blank += 1
            
            if like > max_like or (like == max_like and blank > max_blank):
                max_like = like
                max_blank = blank
                best_seat = (i, j)
            
    classroom[best_seat[0]][best_seat[1]] = student_num


satis = 0
for i in range(n):
    for j in range(n):
        student_num = classroom[i][j]
        like_1, like_2, like_3, like_4 = like_students[student_num][0]
        like = 0
        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < n and 0 <= nj < n:
                if classroom[ni][nj] in (like_1, like_2, like_3, like_4):
                    like += 1
        if like > 0:
            satis += 10**(like-1)

print(satis)