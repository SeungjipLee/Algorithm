def solution(keymap, targets):
    answer = []
    dict = {}
    
    for key in keymap:
        i = 0
        for char in key:
            i += 1
            if dict.get(char):
                dict[char] = min(dict[char], i)
            else:
                dict[char] = i
    for target in targets:
        clicks = 0
        for char in target:
            if dict.get(char):
                clicks += dict[char]
            else:
                answer.append(-1)
                break
        else:
            answer.append(clicks)
    return answer