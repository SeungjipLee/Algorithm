import sys
import heapq
def minput(): return map(int, sys.stdin.readline().split())

### 어떤 수를 고르는가?
## 포함된 구간이 적은 것
## 수를 고르는 우선순위
# 짧은 범위를 가지는 구간의 시작과 끝
# 근데 앞뒤를 자르고 남은 구간은 포함된 수가 더 있는거지
# 같은 범위를 가졌다면 자른 횟수를 보고 우선순위 결정
# 구간마다 최대 100개 까지 정답칸에 넣기
# 근데 해당 숫자가 가지는 구간수를 구할때 엄청 큰 수가 들어 갈 수도 있음..


# 포함된 구간 수가 같은데 범위가 다른경우가 있으면 어떻게 함??
L = int(input())
arr = sorted(list(minput()))
intervals = []
N = int(input())
answer = [*arr]
values = []
for i in range(L):
    if i == 0:
        if arr[i] == 2:
            answer.append(1)
        elif arr[i] > 2:
            intervals.append([1, arr[i]-1])
    else:
        if arr[i] - arr[i-1] == 1:
            continue
        elif arr[i] - arr[i-1] == 2:
            answer.append(arr[i-1]+1)
            continue
        intervals.append([arr[i-1]+1, arr[i]-1])
# print(intervals)
## 구간마다 최대 100개 씩만 뽑아서 arr에 넣고 잘라서 제출?
for interval in intervals:
    s = interval[0]
    e = interval[1]
    cnt = 0
    if interval[1] - interval[0] < 104:
        for num in range(interval[0], interval[1]+1):
            cnt += 1
            size = (e-num+1) * (num-s) + (e-num)
            values.append([size, num])
    else:
        i = 0
        while i != 51:
            num = s + i
            size = (e-num+1) * (num-s) + (e-num)
            values.append([size, num])
            num = e - i
            size = (e-num+1) * (num-s) + (e-num)
            values.append([size, num])
            i += 1

values.sort(key=lambda x: x[1])
values.sort(key=lambda x: x[0])

answer.sort()

# print(values)
for v in values:
    answer.append(v[1])
# print(answer)
for i in range(arr[-1]+1, arr[-1]+101):
    answer.append(i)
    
print(*answer[:N])

# 2~7 구간이 있다고 치자
# 그럼 3이 포함된 구간 수는??
# 23 24 25 26 27 34 35 36 37 | 9
# 2 ~ 10
# 4
# 23 24 25 26 27 28 29 30
# 45 46 47 48 49 410
# 내 앞의 수 | (마지막수 - 나 + 1) * (나 - 맨앞) = 10 -2 = 8
# 내 뒤의 수 | 마지막수 - 나 = 10 -4 = 6
# 2~10 2, 10 을 뺐어 그래서 3~9가 됐어
# 5 6*3 + 5
# 4 7*2 + 6
# 3 8*1 + 7
# 2 8
