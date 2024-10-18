def solution(s):
    answer = []
    
    arr = []
    tmp = []
    tmp_str = ""
    for char in s[1:-1]:
        
        if char == "{":
            tmp =[]
        elif char == ",":
            if tmp_str:
                tmp.append(int(tmp_str))
            tmp_str = ""
        elif char == "}":
            if tmp_str:
                tmp.append(int(tmp_str))
            tmp_str = ""
            arr.append(tmp)
        else:
            tmp_str += char
        # print(char, tmp_str)
    # print(arr)
    arr.sort(key=lambda x: len(x))
    d = {}
    for _arr in arr:
        # print(_arr, d)
        for num in _arr:
            
            if d.get(num) == None:
                answer.append(num)
                d[num] = True
                
                
    
    return answer