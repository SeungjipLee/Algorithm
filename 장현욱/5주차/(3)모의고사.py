# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.


# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예

def solution(answers):
    # 문제 번호 순환
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 쓸 번호의 순서와 현재의 맞은 갯수
    count = [0, 0, 0]
    answer_ing = [0, 0, 0]

    # 최고점과 결과
    best = 0
    answer = []

    for i in answers:
        # 문제가 맞으면 점수 +
        if a1[count[0]] == i:
            answer_ing[0] += 1
        
        if a2[count[1]] == i:
            answer_ing[1] += 1
        
        if a3[count[2]] == i:
            answer_ing[2] += 1

        # 다음 찍을 번호로 이동
        count[0] += 1
        count[1] += 1
        count[2] += 1

        # 만약 길이가 초과된다면 0으로 초기화
        if count[0] == len(a1):
            count[0] = 0
        if count[1] == len(a2):
            count[1] = 0
        if count[2] == len(a3):
            count[2] = 0

    # 가장 많은 문제를 맞춘 사람을 구하기
    for j in range(len(answer_ing)):
        if best == answer_ing[j]:
            answer.append(j+1)
        elif best < answer_ing[j]:
            answer = [j+1]
            best = answer_ing[j]

    return answer