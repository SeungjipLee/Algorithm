'''
점 3개로 삼각형을 만들 수 있음
삼각형의 변중 가장 큰것 * 2 - 가장 작은것 * 2
'''
ls = list(map(int, input().split()))
if (ls[3]-ls[1])*(ls[4]-ls[0]) == (ls[5]-ls[1])*(ls[2]-ls[0]):
    print(-1.0)
else:
    dists = []

    for i in range(2):
        for j in range(i+1, 3):
            ax = ls[2*i]
            ay = ls[2*i+1]
            bx = ls[2*j]
            by = ls[2*j+1]
            dist = ((ax-bx)**2 + (ay-by)**2)**(1/2)
            dists.append(dist)

    print(max(dists)*2 - min(dists)*2)