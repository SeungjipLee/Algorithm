word = "AAAE"
answer = 0
li = [0] * 5
info = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
step = {4: 781, 3: 156, 2: 31, 1: 6, 0: 1}
for i in range(len(word)):
    li[i] = word[i]

print(li)
"""
    1 =>   1가지
   1x =>   5가지
  1xx =>  25가지
 1xxx => 125가지 
1xxxx => 625가지


처음 0인경우 1가지
아닌 경우 30가지 

781개씩
"""
n = 4
for i in li:
    if i:
        answer += info[i]*step[n]
        n -= 1
        answer += 1

print(answer)