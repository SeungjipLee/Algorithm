def solution(s):
    answer = 0
    stack = []
    
    delete_pair(stack, s)
    # while True:
    #     deleted = 
    #     s = "".join(stack)
    #     if not deleted:
    #         break

    if stack:
        return 0
    else:
        return 1

def delete_pair(stack, s):
    deleted = False
    for al in s:
        if stack and stack[-1] == al:
            stack.pop()
            deleted = True
        else:
            stack.append(al)
            
    return deleted