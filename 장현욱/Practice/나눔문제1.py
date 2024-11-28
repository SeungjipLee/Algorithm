import sys

# input.txt 파일을 입력으로 사용
sys.stdin = open("input.txt", "r")

# 1. 첫 번째 줄: 암호문 읽기
pw = input().strip()

# 2. 두 번째 줄 이후: 변환 규칙 읽기
n = int(input().strip())  # 변환 규칙의 개수
rules = []

for _ in range(n):
    # 변환 규칙을 읽어 리스트로 저장
    x, y = input().strip().split()
    rules.append([x, y])

# 확인용 출력
print("암호문:", pw)
print("변환 규칙:", n)
print(rules)
# 암호문

# word = [x for x in rules[count] if x != i][0]


def solution(pw, how, rules):
    answer = ''
    for i in pw:  # 패스워드 하나씩 돌기
        word = i  # 현재의 글자 복사해두기
        visited = [0] * how  # 9개의 리스트 만들기
        count = 0
        switch = 1
        lastcount = 99999999
        while switch:
            print('현재카운트',count, '현재 글자', word, '마지막장소',lastcount)
            if word in rules[count]:
                if visited[count] == 0:
                    visited[count] = 1
                    word = [x for x in rules[count] if x != word][0]  # 현재의 단어외의 나머지
                    lastcount = count
                    count += 1
                else:
                    if lastcount == count:
                        break
                    else:
                      word = '?'
                      break
            else:
                count += 1
            if count == how:
                if 1 in visited:
                    count = 0
                else:
                    break
        
        answer += word
        lastcount = 9999

    return answer



print("정답",solution(pw, n, rules))