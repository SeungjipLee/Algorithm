cnt = 0
answer = 0
def solution(word):
    global cnt
    global answer 
    arr = ["A", "E", "I", "O", "U"]
    
    make_word("", word, arr)
    
    return answer

def make_word(tmp, word, arr):
    global cnt
    global answer
    # print(tmp, cnt)
    if tmp == word:
        answer = cnt
        # print(tmp, answer)
        return
    
    if len(tmp) == 5:
        return
    
    for al in arr:
        cnt += 1
        make_word(tmp+al, word, arr)
    
    
    