clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

"""
헤드기어 : yellow_hat | green_turban
안경류 : blue_sunglasses

최소 1가지는 입어야한다

1
2
3
13
23

이렇게 총 5가지?
3 * 2 - 1 = 5 하면 되는거 아님?

페이스 : 크로우마스크, 파란 선글라스, 스모키 화장

총 3가지
4 * 1 - 1 = 3
"""

whole = dict()
for i in clothes:
    if i[1] in whole:
        whole[i[1]].append(i[0])
    else:
        whole[i[1]] = [i[0]]



answer = 1
for i in whole:
    mid *= len(whole[i]) + 1

