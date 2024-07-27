def solution(s, n):
    answer = ''
    for i in s:
        # 공백이면 더하고
        if i == " ":
            answer += i
        # 대문자면(65~90)    
        elif 65 <= ord(i) <= 90:
            j = ((ord(i) + n) - 65) % 26 + 65
            answer += chr(j)
        else:
            j = ((ord(i) + n) - 97) % 26 + 97
            answer += chr(j)

    return answer

print(solution("AB", 4))