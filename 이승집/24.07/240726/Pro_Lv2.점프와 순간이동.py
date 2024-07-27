"""
순간이동(2배 이동)은 건전지가 0이 들고
k칸 이동은 건전지가 k만큼 든다
최소한으로 건전지를 사용하여 목적지까지 이동하라

5000 만큼의 list를 만들고

"""

def solution(n):
    cnt=1
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n-1
            cnt+=1
    return cnt

N = 100
distance = [0] * (N + 1)
distance[1] = 1
for i in range(1, N + 1):
    if distance[i] != 0:
        mid = i
        while mid * 2 <= N:
            distance[mid * 2] = distance[i]
            mid *= 2
    else:
        idx = 1
        while distance[i - idx] == 0:
            idx += 1
        distance[i] = distance[i-idx] + idx
        mid = i
        while mid * 2 <= N:
            distance[mid * 2] = distance[i]
            mid *= 2

print(distance)
print(solution(5000))