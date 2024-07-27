"""
[큰거, 작은거]
brown(테두리) = 24
yellow(중앙) = 24

1. 두 개의 합이 전체 넓이가 되고 그 중에 후보를 고르면 된다
2. brown으로 걸러야? / yellow로 걸러야?
"""

brown = 24
yellow = 24

whole = brown + yellow

for i in range(1, whole + 1):
    if whole%i == 0 and (whole//i + i)*2 - 4 == brown:
        print([whole//i, i])
        break