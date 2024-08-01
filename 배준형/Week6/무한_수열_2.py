import sys, math
def minput(): return map(int, sys.stdin.readline().split())

N, P, Q, X, Y = minput()

if N == 0:
    print(1)
    exit()
p_ = int(math.log(N, P)) + 1
q_ = int(math.log(N, Q)) + 1
dp = {}
dp[0] = 1

arr = []
def find_idx(num):
    if num <= 0:
        return 1
    if dp.get(num):
        return dp[num]

    dp[num] = find_idx(num//P-X) + find_idx(num//Q-Y)
    return dp[num]

print(find_idx(N))
# arr = []
# def find_idx(num):
#     if num <= 0:
#         return 1

#     return find_idx(num//P-X) + find_idx(num//Q-Y)

# print(find_idx(N))

# arr = sorted(list(set(arr)))

# for a in arr:
#     if a <= 0:
#         continue

#     x = a//P-X
#     y = a//Q-Y

#     if x < 0:
#         x = 1
#     else:
#         x = dp[a//P-X]

#     if y < 0:
#         y = 1
#     else:
#         y = dp[a//Q-Y]

#     dp[a] = x + y

# print(dp[N])
# idxs = []
# for i in range(p_+1):
#     for j in range(q_+1):
#         tmp = N // (P**i * Q**j)
#         idxs.append(tmp)
#         idxs.append(tmp - X) 
#         idxs.append(tmp - Y)

# idxs = list(set(idxs))
# idxs.sort()
# print(idxs)
# for idx in idxs:
#     if idx <= 0:
#         continue

#     x = idx//P-X
#     y = idx//Q-Y

#     if x < 0:
#         x = 1
#     else:
#         x = dp[idx//P-X]

#     if y < 0:
#         y = 1
#     else:
#         y = dp[idx//Q-Y]

#     dp[idx] = x + y

# print(dp[N])