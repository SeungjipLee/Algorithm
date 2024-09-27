# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 
# 길이 5 이하의 모든 단어가 수록되어 있습니다. 
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.
# 단어 하나 word가 매개변수로 주어질 때, 
# 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

def solution(word):
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']  # 사용가능한 단어
    found = False  # 스위치
    def dfs(length, now_word):
        nonlocal answer, found  # aswer와 found의 지역변수가 아님을 선언
        if length == 5:  # 길이가 5 를 넘어가지 않게 만들기
            return
        if found:  # 찾으면 리턴
            return
        else:
            for i in range(len(words)):  # 단어 하나씩 재귀함수
                answer += 1
                if now_word + words[i] == word:
                    found = True
                    return
                dfs(length + 1, now_word + words[i])
                if found:
                    return
    dfs(0, '')
                
    return answer