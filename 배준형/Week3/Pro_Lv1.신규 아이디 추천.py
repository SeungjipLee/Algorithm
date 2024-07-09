def solution(new_id):
    answer = ''
    id_arr = list(new_id)
    len_id = len(id_arr)
    id_is_avail = [1] * len_id
    
    # 대문자를 소문자로 + 사용불가능한 문자 제거
    for i in range(len_id):
        if id_arr[i].isupper():
            id_arr[i] = id_arr[i].lower()
        if id_arr[i].isalpha() or id_arr[i].isdigit() or id_arr[i] in "-_.":
            continue
        id_is_avail[i] = 0
    
    pre = ''
    for i in range(len_id):
        if pre == '' and id_arr[i] == '.':
            continue
        if pre == '.' and id_arr[i] == '.':
            continue
        if id_is_avail[i]:
            pre = id_arr[i]
            answer += id_arr[i]
       
    if not answer:
        answer = 'a'
    else:
        len_answer = len(answer)
        while answer[-1] == '.':
            answer = answer[:len_answer]
            len_answer -= 1
        
    if len(answer) > 15:
        answer = answer[:15]
        i = 14
        while answer[i] == '.':
            answer = answer[:i]
            i -= 1
            
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    return answer