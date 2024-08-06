from itertools import product

n = 1
info = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 인덱스와 점수를 동일시 하기 위해
info.reverse()
ans = [-1]
div = 0

# 각 점수당 이기거나 지거나의 경우로 나누자
for case in product((True, False), repeat=11):
    t = 0
    # 이길때 필요한 화살의 개수의 합
    need = sum(info[i] + 1 for i in range(11) if case[i])
    # 최대 화살 수 보다 작은 경우만 카운팅
    if need <= n:
        # 어피치는 False이면서 0이 아닌 값들의 합
        # 라이언은 True일때의 값의 합
        apeach = sum(i for i in range(11) if not case[i] and info[i])
        ryan = sum(i for i in range(11) if case[i])
        mid_div = ryan - apeach
        if mid_div > div:
            div = mid_div
            ans = [info[i]+1 if case[i] else 0 for i in range(11)]
            ans[0] += n - need
ans.reverse()
print(ans)

