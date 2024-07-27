from datetime import date

day = {0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"}


def solution(a, b):
    answer = date(2016, a, b).weekday
    return answer


print(solution(5, 24))
