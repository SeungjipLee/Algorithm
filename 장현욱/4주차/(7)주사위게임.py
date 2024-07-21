# 1부터 6까지 숫자가 적힌 주사위가 3개
# 각각 굴려서
# 숫자모두 다르면 a+b+c
# 두숫자는 같고 나머지는 다르면 (a+b+c) *(a**2 + b**2 + c**2)
# 세숫자가 모두 같다면 
# (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)

def solution(a, b, c):
    answer = 0
    if a == b and b == c:
        answer = (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or b == c or a == c:
        answer = (a+b+c) *(a**2 + b**2 + c**2)
    else :
        answer = a + b + c
    return answer


# 방법2
def solution(a, b, c):
    check=len(set([a,b,c])) # set은 클래스이므로 list로 감싸주기
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)
