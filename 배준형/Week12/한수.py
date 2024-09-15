import sys
input_ = sys.stdin.readline

# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 
# 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
# N이 주어졌을 때, 
# 1보다 크거나 같고, N보다 작거나 같은 
# 한수의 개수를 출력하는 프로그램을 작성하시오. 

def solution():
    N = int(input_())

    if N < 100:
        print(N)
    else:
        answer = 99
        for i in range(100, N+1):
            if is_seq(i):
                answer += 1
        print(answer)


def is_seq(num):
    num = [int(i) for i in list(str(num))]
    pre = num[1]
    d = num[1] - num[0]
    for n in num[2:]:
        if n - pre != d:
            return False
        pre = n

    return True

solution()