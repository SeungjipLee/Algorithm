import math

def solution(w, h):
    temp = max(w, h) / min(w, h)
    temp = 1.000000000000000000000000001
    k = math.ceil(temp - 1e-9)  # 작은 값을 더해 부동 소수점 오류 방지
    answer = w * h - k * min(w, h)
    return answer

temp = 1.000000000000000000000000001
# Consider very small epsilon to handle floating point inaccuracies
epsilon = 1e-10
if temp > 1 and temp - int(temp) < epsilon:
    k = int(temp) + 1
else:
    k = math.ceil(temp)
print(k)