import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    terr = list(map(int, input().split()))
    my_dict = {}
    for i in range(1, terr[0]+1):
        if my_dict.get(terr[i]) == None:
            my_dict[terr[i]] = 1
        else:
            my_dict[terr[i]] += 1
            if my_dict[terr[i]] > terr[0] / 2:
                print(terr[i])
                break
    else:
        print("SYJKGW")

    