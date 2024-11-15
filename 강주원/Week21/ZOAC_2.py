st = input()
# 처음에 cur 는 A, ord('A) = 65
alphabet = {chr(i):i-64 for i in range(65, 65+26)}
def find_min_time(cur, s):
    a, b = alphabet[cur], alphabet[s]
    min_val = min(abs(a - b), 26-a+b, 26-b+a)
    return min_val

cur = 'A'
res = 0
for i in st:
    res += find_min_time(cur, i)
    cur = i

print(res)
