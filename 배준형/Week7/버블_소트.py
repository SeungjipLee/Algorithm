# 버블 소트
# 첫번째 원소부터 인접한 원소와 비교해서 한칸씩 뒤로 이동
# 인접한 원소와 바꾸는(swap) 총 횟수를 출력

# N 1~500,000
# 실제로 버블소트하면 O(N^2) 이라 시간초과

# 어떻게 하면 swap 횟수를 모두 체크할 수 있는가..

# 3 2 | 1
# 2 3 | 1
# 1 2 3

# 카테고리 : 분할정복, 세그먼트트리, 정렬

# 병합 정렬 하면서 앞질러가는 애들 몇개 앞지르는지 개수 체크하기
import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

def merge_sort(arr, s, e):

    global answer
    
    if s == e:
        return [arr[s]]
    
    mid = (s+e)//2
    
    left = merge_sort(arr, s, mid)
    right = merge_sort(arr, mid+1, e)
    len_left = len(left)
    len_right = len(right)
    li = 0
    ri = 0
    tmp = []
    
    while li != len_left or ri != len_right:
        if li != len_left and ri != len_right:
            if left[li] > right[ri]:
                tmp.append(right[ri])
                ri += 1
                answer += len_left - li
            else:
                tmp.append(left[li])
                li += 1
        elif li != len_left:
            tmp.append(left[li])
            li += 1
        elif ri != len_right:
            tmp.append(right[ri])
            ri += 1
    return tmp
    
    

# 왼쪽에 몇개 있는지를 알아야 이동할 때 더해줄 수 있음
N = int(input_())
arr = list(minput())

answer = 0

sorted_arr = merge_sort(arr, 0, N-1)
# print(sorted_arr)
print(answer)