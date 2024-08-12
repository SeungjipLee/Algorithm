str1, str2 = "aa1+aa2", "AAAA12"

"""
A = {fr ra an nc ce}
B = {fr re en nc ch}

97 ~ 122
"""
str1, str2 = str1.lower(), str2.lower()

St1 = dict()
St2 = dict()
sum1 = 0
sum2 = 0


for i in range(len(str1) - 1):
    if 97 <= ord(str1[i]) <= 122 and 97 <= ord(str1[i + 1]) <= 122:
        mid = str1[i] + str1[i + 1]
        if mid in St1:
            St1[mid] += 1
            sum1 += 1
        else:
            St1[mid] = 1
            sum1 += 1

for i in range(len(str2) - 1):
    if 97 <= ord(str2[i]) <= 122 and 97 <= ord(str2[i + 1]) <= 122:
        mid = str2[i] + str2[i + 1]
        if mid in St2:
            St2[mid] += 1
            sum2 += 1
        else:
            St2[mid] = 1
            sum2 += 1

# print(St1, sum1)
# print(St2, sum2)

common = 0
# 교집합 구하기
for i in St1:
    if i in St2:
        common += min(St1[i], St2[i])

if sum1 == 0 and sum2 == 0:
    print(65536)
else:
    print(int((common/(sum1 + sum2 - common))*65536))
