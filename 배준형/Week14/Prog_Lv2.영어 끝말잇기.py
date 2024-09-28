def solution(n, words):
    answer = [0, 0]
    used = {}
    pre = ""
    for idx, word in enumerate(words):
        if pre == "":
            pre = word[-1]
            used[word] = True
            continue
        if pre != word[0] or used.get(word) != None:
            answer = [idx%n+1, idx//n+1]
            break
        # print(word)
        pre = word[-1]
        used[word] = True
            
    return answer