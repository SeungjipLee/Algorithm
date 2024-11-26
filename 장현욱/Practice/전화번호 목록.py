# 전화번호부에 적힌 전화번호 중, 
# 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 
# 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 
# false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.


# 1차 풀이 2중포문으로 시간초과
def solution(phone_book):
    answer = True
    # 1. 2중 for문을 사용할건데 처음 번호의 len만큼만 가도록 해서
    for i in range(len(phone_book)):
        i_len = len(phone_book[i])
        now_i = phone_book[i]
        for j in range(i + 1, len(phone_book)): # i+1부터 시작하는거 잊지말기
            j_len = len(phone_book[j])
            now_j = phone_book[j]
            if i_len <= j_len:
                # j_len이 i_len의 갯수까지 똑같은지 확인
                if now_i == now_j[:i_len]:
                    return False
                    
            else:
                if now_i[:j_len] == now_j:
                    return False
                # i_len이 j_len의 갯수까지 똑같은지 확인
    return answer

# 2차 풀이 정렬을 이용한 가까운 숫자와만 비교
def solution(phone_book):
    # 1. phone_book 정렬
    phone_book.sort()

    # 2. 정렬된 리스트에서 인접한 문자열 비교
    for i in range(len(phone_book) - 1):
        # 현재 번호가 다음 번호의 접두어인지 확인
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False

    # 3. 접두어 관계가 없으면 True 반환
    return True
