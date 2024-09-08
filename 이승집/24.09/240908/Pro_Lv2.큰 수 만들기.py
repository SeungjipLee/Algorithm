number = "4177252841"
k = 4
answer = ""

"""
4177252841
k = 4
정답 = 6

41772 => 최댓값 7
-2

725 => 최댓값 7
-0

252 => 최댓값 5
-1

28 => 최댓값 -1

끝 뒤에 이어 붙이기
"""

# idx = 0
# while k:
#     M = list(map(int, number[idx:idx + k + 1]))
#     if M:
#         m = max(M)
#         n = 0
#         while int(number[idx + n]) != m:
#             n += 1
#         k -= n
#         answer += number[idx + n]
#         idx += n + 1
#         print(answer)
#     else:
#         break
#
# answer += number[idx:]
# print(answer)


def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


print(solution(number, k))
