# 정수가 담긴 리스트 num_list가 주어질 때, 
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 
# return하도록 solution 함수를 완성해주세요.

# 모든 리스트의 곱 < 모든리스트합의제곱 1 아님 0

def solution(num_list):
    answer = 0
    a = num_list[0]
    b = 0
    for i in range(1, len(num_list)):
        a = a * num_list[i]
    for k in num_list:
        b += k
    b = b ** 2
    if a<b:
        answer = 1
    return answer

# 2안
def solution(num_list):
    a=1
    b=0
    for x in num_list:
        a*=x
        b+=x
    if a<b*b: return 1
    return 0