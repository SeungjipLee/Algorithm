from collections import defaultdict

def solution(msg):
    answer = []
    dict_ = defaultdict(int)
    for i in range(1, 27):
        dict_[chr(i+64)] = i
    
    idx = 0
    key = 27
    n = len(msg)
    
    while True:
        # print("loop start", n, idx)
        l_string, length = find_longest_string(dict_, msg[idx:])
        if not dict_[msg[idx:idx+length+1]]:
            dict_[msg[idx:idx+length+1]] = key
        answer.append(dict_[msg[idx:idx+length]])
        key += 1
        idx += length
        # print(dict_)
        if idx >= n:
            # print("stopped")
            break
        # print(l_string, length, answer)
    
    return answer

def find_longest_string(dict_, word):
    # print("here", word)
    tmp = ""
    if len(word) == 1:
        return word, 1
    for w in word:
        if dict_[tmp+w] == 0:
            break
        tmp += w
    return tmp, len(tmp)
        
print(solution("KAKAO")) # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]