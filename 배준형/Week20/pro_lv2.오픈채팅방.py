def solution(record):
    answer = []
    stack = []
    d = {}
    for reco in record:
        cmd, *id_ = reco.split()
        if cmd == "Enter":
            stack.append([cmd, id_[0]])
            d[id_[0]] = id_[1]
        elif cmd == "Leave":
            stack.append([cmd, id_[0]])
        elif cmd == "Change":
            d[id_[0]] = id_[1]
            
    for s in stack:
        if s[0] == "Enter":
            answer.append(d[s[1]]+"님이 들어왔습니다.")
        else:
            answer.append(d[s[1]]+"님이 나갔습니다.")
        
    return answer