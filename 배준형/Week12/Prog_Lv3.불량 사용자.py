def solution(user_id, banned_id):
    answer = 0
    n = len(user_id)
    m = len(banned_id)
    banned_ids = [[] for _ in range(m)]
    # 1. 각 banned_id 에 가능한 아이디들 다 찾아두기
    for i in range(m):
        banned_ids[i].extend(id_check(banned_id[i], user_id))

    # 2. 가능한 조합 => 비트마스킹으로 만들어서 갯수 세기
    combs = []
    make_comb(combs, banned_ids, 0, 0, m)
    
    return len(set(combs))

def id_check(b_id, user_id):
    result = []
    length = len(b_id)
    for i, u_id in enumerate(user_id):
        if len(u_id) != length:
            continue
        for idx, each in enumerate(b_id):
            if each == "*":
                continue
            if u_id[idx] != each:
                break
        else:
            result.append(i)    

    return result

def make_comb(combs, banned_ids, comb, d, m):
    if d == m:
        combs.append(comb)
        return
    ids = banned_ids[d]

    for now in ids:
        if 1<<now & comb:
            continue
        make_comb(combs, banned_ids, comb|1<<now, d+1, m)
