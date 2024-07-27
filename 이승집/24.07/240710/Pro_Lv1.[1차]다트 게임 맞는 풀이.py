import re


def solution(dartResult):
    # 정규 표현식을 사용하여 각 점수 기회를 추출합니다.
    dart_results = re.findall(r'\d{1,2}[SDT][*#]?', dartResult)
    print(dart_results)

    scores = []
    for dart in dart_results:
        # 각 기회에 대한 점수와 옵션을 초기화합니다.
        score = 0
        option = ''

        # 숫자 부분과 SDT 부분을 분리합니다.
        match = re.match(r'(\d{1,2})([SDT])([*#]?)', dart)
        num = int(match.group(1))
        bonus = match.group(2)
        option = match.group(3)

        # 점수 계산
        if bonus == 'S':
            score = num ** 1
        elif bonus == 'D':
            score = num ** 2
        elif bonus == 'T':
            score = num ** 3

        # 옵션 처리
        if option == '*':
            score *= 2
            if scores:
                scores[-1] *= 2
        elif option == '#':
            score *= -1

        scores.append(score)

    return sum(scores)

print(solution("1D2S#10S"))