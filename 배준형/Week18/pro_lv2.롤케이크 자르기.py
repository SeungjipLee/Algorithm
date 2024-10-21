def solution(topping):
    answer = 0
    n = len(topping)
    cs = [0] * n
    bro = [0] * n
    d = {}
    d[topping[0]] = True
    cs[0] = 1 
    b = {}
    b[topping[-1]] = True
    bro[n-1] = 1
    
    for i in range(1, n):
        if d.get(topping[i]) == None:
            d[topping[i]] = True
            cs[i] = cs[i-1] + 1
        else:
            cs[i] = cs[i-1]
        
        if b.get(topping[n-1-i]) == None:
            b[topping[n-1-i]] = True
            bro[n-1-i] = bro[n-i] + 1
        else:
            bro[n-1-i] = bro[n-i]
    
    # print(cs)
    # print(bro)
    for i in range(n-1):
        if cs[i] == bro[i+1]:
            answer += 1

    return answer