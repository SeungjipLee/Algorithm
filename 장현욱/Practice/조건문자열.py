# 두 수의 크기를 비교
# ><
# !=
# number
# 가 들어감
# true = 1 flase = 0

def solution(ineq, eq, n, m):
    if eq == '=':
        if ineq == '>':
            return int(n >= m)
        else :
            return int(n <= m)
    else:
        if ineq == '>':
            return int(n > m)
        else :
            return int(n < m)
