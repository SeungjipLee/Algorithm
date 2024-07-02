def solution(players, callings):
    answer = []
    l = len(players)
    pre = [i for i in range(-1, l-1)]
    post = [i for i in range(1, l+1)]
    post[l-1] = -1
    p_dict = {}
    
    for i in range(l):
        p_dict[players[i]] = i
    
    for call in callings:

        na = p_dict[call]            
        ab = pre[na]
        dui = post[na]
        abab = pre[pre[na]]
        if abab != -1:
            post[abab] = na    
        if dui != -1:
            pre[dui] = ab    
            
        pre[ab] = na
        post[na] = ab
        post[ab] = dui
        pre[na] = abab

    first = -99
    for i in range(l):
        if pre[i] == -1:
            first = i
    
    answer.append(players[first])
    
    nxt = first
    while True:
        if post[nxt] == -1:
            break
        answer.append(players[post[nxt]])
        nxt = post[nxt]
    
    return answer