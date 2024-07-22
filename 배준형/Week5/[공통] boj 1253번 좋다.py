import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

def lower_bound(a, t, s, e):
    if s >= e:
        return e
    mid = (s+e) // 2

    if t <= a[mid]:
        return lower_bound(a, t, s, mid)
    return lower_bound(a, t, mid+1, e)

N = int(input_())
arr = list(minput())
arr.sort()
answer = 0
for i in range(N):
    now = arr[i]
    made = False
    for j in range(N):
        if made:
            break
        if i == j:
            continue
        num1 = arr[j]
        target = now - num1
        # print(now, num1, target)
        # 첫번째 포인터는 다음거 
        lb = lower_bound(arr, target, 0, N-1)
        for k in range(lb, N):
            
            if k == i or k == j:
                continue
            # 두번째 포인터는 차를 lower_bound 로 찾기
            if arr[k] > target:
                break
            if arr[k] == target:
                # print(i, j, k)
                answer += 1
                made = True
                break

print(answer)


# 예외상황이 너무많네..
# N = list(minput())[0]
# arr = list(minput())
# arr.sort()
# # 다른 수 두 개의 합이 arr 안에 있다면 그 수 는 좋다
# # 좋다가 몇 개인가?
# arr_dict = {}
# arr_cnt = {}
# max_num = arr[-1]
# for item in arr:
#     arr_dict[item] = False
#     if arr_cnt.get(item):
#         arr_cnt[item] += 1
#     else:
#         arr_cnt[item] = 1
# # 수는 최대 2000개
# # 수의 크기는 최대 10억
# answer = 0 
# for i in range(N):
#     for j in range(i+1, N):
#         a = arr[i]
#         b = arr[j]
#         tmp = a + b
#         if a == 0 and b != 0:
#             if arr_cnt[b] < 2:
#                 continue
#         if a != 0 and b == 0:
#             if arr_cnt[a] < 2:
#                 continue
#         if tmp > max_num:
#             continue
#         if arr_dict.get(tmp) != None:
#             arr_dict[tmp] = True

# for key in arr_dict:
#     if key == 0 and arr_cnt[key] <= 2:
#         continue
#     if arr_dict[key]:
#         answer += arr_cnt[key]

# print(answer)
