def solution(s):
    answer = len(s)
    N = len(s)

    for l in range(1, N + 1):
        mid = ""
        stack = []

        for i in range(0, N, l):
            now_s = s[i:i + l]

            if not stack or stack[-1] == now_s:
                stack.append(now_s)
            else:
                if len(stack) == 1:
                    mid += stack[-1]
                else:
                    mid += f'{len(stack)}{stack[-1]}'
                stack = [now_s]

        if len(stack) == 1:
            mid += stack[-1]
        else:
            mid += f'{len(stack)}{stack[-1]}'

        if len(mid) < answer:
            answer = len(mid)

    return answer