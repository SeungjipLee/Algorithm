import sys
input = sys.stdin.readline
X, Y = map(int,input().split())
Z = int((Y/X)*100)
old = int((Y/X)*100)
left, right = 0,X
ans = []
if Z >= 100:
    print(-1)
else:
    while left <= right:
        #mid값 구하고 X랑 Y에 계속 mid값 더하면서 승률Z가 변하는지, 변하면 그 값중 최소값
        newX, newY = X, Y
        mid = (left+right)//2
        newX+=mid
        newY+=mid
        Z = int((newY/newX)*100)
        #Z가 변하는지만 체크하면 되니까 여기 if문을 좀 변형했는데 여기서 이상한건가?
        #Z가 안변하면 무조건 mid값을 늘려야 하니까 원본값old랑 변한 값 Z비교해서
        #같으면 left = mid+1
        if Z==old:
            left = mid+1
        else:
            #Z를 변하게 한 mid값 일단 리스트에 저장하고 최소값 찾기 위해 mid줄여나감
            ans.append(mid)
            right = mid-1
    print(min(ans))