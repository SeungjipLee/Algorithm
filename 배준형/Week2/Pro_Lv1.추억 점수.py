def solution(name, yearning, photo):
    answer = []
    l = len(name)
    dict = {}
    for i in range(l):
        dict[name[i]] = yearning[i]
        
    for result in photo:
        total = 0
        for who in result:
            if dict.get(who):
                total += dict[who]
        answer.append(total)
        
    return answer