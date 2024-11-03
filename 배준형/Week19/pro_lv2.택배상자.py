def solution(order):
    answer = 0
    stack = []
    box = 1
    
    for now in order:
        
        if now == box:
            answer += 1
            box += 1
            continue
        if stack and stack[-1] == now:
            stack.pop()
            answer += 1
            continue
        if now > box:
            for i in range(box, now):
                stack.append(i)
            box = now + 1
            answer += 1
        else:
            break
        # print(now, box, stack)

    return answer