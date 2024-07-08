def solution(today, terms, privacies):
    
    answer = []
    year, month, day = map(int, today.split("."))
    
    terms_dict = {}
    
    for term in terms:
        type_of, period = term.split()
        terms_dict[type_of] = int(period) * 28
    
    i = 0
    for privacy in privacies:
        i += 1
        join_date, type_of_p = privacy.split()
        y, m, d = map(int, join_date.split("."))
        
        d += terms_dict[type_of_p]
        
        while d > 28:
            d -= 28
            m += 1
            if m > 12:
                y += 1
                m = 1
        
        if y == year:
            if m == month:
                if d <= day:
                    answer.append(i)
            elif m < month:
                answer.append(i)
        elif y < year:
            answer.append(i)
    return answer