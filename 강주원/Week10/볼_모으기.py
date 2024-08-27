import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

l, r = s[0], s[-1]
my_dict = {'R':s.count('R'), 'B':s.count('B')}

# 왼쪽
l_cnt = 0
for i in s:
    if i != l:
        break
    l_cnt += 1

L = my_dict[l] - l_cnt

# 오른쪽
r_cnt = 0
for i in s[::-1]:
    if i != r:
        break
    r_cnt += 1

R = my_dict[r] - r_cnt

# 양 끝이 같은 문자일 때 가능한 케이스
toggle = {'R':'B', 'B':'R'}
center = 1e9
if l == r:
    center = my_dict[toggle[l]]

print(min(L, R, center))