def solution(s, skip, index):

    answer = ''
    alpha = [0] * 26
    for skipped in skip:
        alpha[ord(skipped) - 97] = 1
    # print(alpha)
    
    for char in s:
        now = ord(char) - 97
        # print(char, now)
        count = 0
        while count != index:
            now += 1
            if now > 25:
                now = 0
            if alpha[now]:
                continue
            count += 1
            
        # print("result", now, chr(now + 97))
        answer += chr(now + 97)
    
    
    return answer


# def solution(s, skip, index):
#     # a 부터 z 까지 0 부터 25의 인덱스를 가짐
#     # 해당 인덱스의 값에는 index 뒤의 알파벳의 번호를 부여
#     answer = ''
#     alpha = []
#     for i in range(index, index+26):
#         if i > 25:
#             i -= 26
#         alpha.append(i)
#     skip = list(set(list(skip)))
#     # print(alpha)
#     for skipped in skip:
        
#         now = ord(skipped) - 97
#         alpha[now] = -1

#         # for i in range(1, index+1):
#         i = 0
#         count = 0
        
#         while count < index:
#             i += 1
#             if now - i < 0:
#                 if alpha[now - i + 26] == -1:
#                     continue
#                 alpha[now - i + 26] += 1    
#                 if alpha[now - i + 26] > 25:
#                     alpha[now - i] = 0
#             else:
#                 if alpha[now - i] == -1:
#                     continue
#                 alpha[now - i] += 1
#                 if alpha[now - i] > 25:
#                     alpha[now - i] = 0
#             count += 1
#         for i in range(26):
#             if alpha[i] == -1:
#                 continue
#             while alpha[alpha[i]] == -1:
#                 alpha[i] += 1
#                 if alpha[i] > 25:
#                     alpha[i] = 0
#         # print(alpha)
            
    
            
#     # print(alpha)
#     for char in s:
#         answer += chr(alpha[ord(char) - 97] + 97)
#     return answer