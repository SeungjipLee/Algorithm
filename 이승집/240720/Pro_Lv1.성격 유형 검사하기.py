
"""
총 n개의 질문
각 질문 당 7개의 선택지

매우 비동의(왼쪽 3점) / 비동의(왼쪽 2점) / 약간 비동의(왼쪽 1점)
모르겠음(점수 0)
약간 동의(오른쪽 1점) / 동의(오른쪽 2점) / 매우 동의(오른쪽 3점)

1번(R : 라이언형 / T : 튜브형)
2번(C : 콘형 / F : 프로도형)
3번(J : 제이지형 / M : 무지형)
4번(A : 어피치형 / N : 네오형)

동점이면 왼쪽 꺼

"RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 로만 구성
"""

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
answer = ""

type_point = {"R": 0, "T": 0, "C": 0, "F": 0,
              "J": 0, "M": 0, "A": 0, "N": 0}

for i in range(len(survey)):
    question_type = survey[i]
    question_choice = choices[i]

    if 1 <= question_choice < 4:
        type_point[question_type[0]] += 4 - question_choice

    else:
        type_point[question_type[1]] += question_choice - 4

if type_point["R"] < type_point["T"]:
    answer += "T"
else:
    answer += "R"

if type_point["C"] < type_point["F"]:
    answer += "F"
else:
    answer += "C"

if type_point["J"] < type_point["M"]:
    answer += "M"
else:
    answer += "J"

if type_point["A"] < type_point["N"]:
    answer += "N"
else:
    answer += "A"

print(answer)