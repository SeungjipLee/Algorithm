today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

answer = []
renewal_terms = renewal_privacies = dict()
compare = "".join(today.split("."))
idx = 1

for i in terms:
    a, b = i.split(" ")
    renewal_terms[a] = int(b)

for i in privacies:
    start, what = i.split(" ")
    date = [int(i) for i in start.split(".")]
    year, month, day = date

    # month를 올려보자
    month += renewal_terms[what]
    while month > 12:
        month -= 12
        year += 1

    # day를 내려보자
    if day == 1:
        day = 28
        month -= 1
        if month == 0:
            month = 12
            year -= 1
    else:
        day -= 1

    here = str(year) + str(month).zfill(2) + str(day).zfill(2)

    if int(compare) > int(here):
        answer.append(idx)
    idx += 1

print(answer)