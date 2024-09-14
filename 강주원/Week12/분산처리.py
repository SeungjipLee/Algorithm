import sys
input = sys.stdin.readline

t = int(input())

arr = [[10], [1], [2,4,8,6], [3,9,7,1], [4,6], [5], [6], [7,9,3,1], [8,4,2,6], [9,1], [10]]
def sol():
    a, b = map(int, input().split())
    a %= 10
    c = b%len(arr[a]) - 1
    print(arr[a][c])


for tc in range(t):
    sol()