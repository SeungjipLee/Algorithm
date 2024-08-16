n = 16   # n진법
t = 16   # t개의 수를 말하면 됨
m = 2   # 참가자 수
p = 1   # 정답자의 순서

"""
2진법이라면
0 1 10 11 100 101 ...

정답자 : 0 1 1 1
반대편 : 1 0 1 0
"""
whole = ""
cnt = 0
num = 0


while cnt < m*t + 1:
    i = num
    mid = ""
    while i >= n:
        if (i%n) >= 10:
            mid = chr(i%n + 55) + mid
        else:
            mid = str(i%n) + mid
            i //= n
    if i >= 10:
        mid = chr(i + 55) + mid
    else:
        mid = str(i) + mid
    whole += mid
    cnt += len(mid)
    num += 1

print(whole, cnt)

answer = ""
for i in range(p-1, len(whole), m):
    answer += whole[i]
print(answer[:t])

"""
def solution(n, t, m, p):
    answer = ""
    num = 0
    length = 0
    
    while len(answer) < t:
        mid = ""
        i = num
        while i > 0:
            if (i % n) >= 10:
                mid = chr(i % n + 55) + mid
            else:
                mid = str(i % n) + mid
            i //= n
        
        # i가 0인 경우에도 '0'이 포함되도록
        if mid == "":
            mid = "0"
        
        # 현재 변환된 숫자 문자열에서 필요한 부분만 추출
        for c in mid:
            if length % m == p - 1:
                answer += c
            length += 1
            
            # 필요한 답의 길이만큼만 얻으면 루프 종료
            if len(answer) == t:
                return answer
        
        num += 1

    return answer

-> 시간 복잡도를 줄이기 위해서 필요한 부분만을 사용하자 그 차이가 생각보다 크다!
"""

