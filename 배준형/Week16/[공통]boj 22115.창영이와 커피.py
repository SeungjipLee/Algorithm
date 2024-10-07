from collections import defaultdict
from collections import Counter
import copy
import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, K = minput()

if K == 0:
    print(0)
    exit()

coffees = list(minput())
coffees.sort()
num_coffee = defaultdict(int)
# dp = [[최소 마신 횟수, {카페인: 개수}]]
# dp[4] = [2, {2: 2}] 라면 4라는 카페인을 충족하기위해 2카페인 커피 2개를 마셨다.
dp = [[int(1e9), defaultdict(int)] for _ in range(100_001)]

for coffee in coffees:
    num_coffee[coffee] += 1
    dp[coffee][0] = 1
    dp[coffee][1][coffee] = 1

coffees = list(set(coffees))

for i in range(100_001):
    if dp[i][0] == int(1e9):
        continue
    
    for coffee in coffees:
        if dp[i][1][coffee] < num_coffee[coffee]:
            if i+coffee > 100_000:
                continue
            if dp[i+coffee][0] > dp[i][0] + 1:
                dp[i+coffee][0] = dp[i][0] + 1
                dp[i+coffee][1] = copy.deepcopy(dp[i][1])
                dp[i+coffee][1][coffee] += 1
# print(dp[:10])

if dp[K][0] == int(1e9):
    print("-1")
else:
    print(dp[K][0])