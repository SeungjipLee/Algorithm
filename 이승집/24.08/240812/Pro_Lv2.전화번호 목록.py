phone_book = ["12", "1 23", "1 2 35", "567", "88"]
phone_book = [i.replace(" ", "") for i in phone_book]

phone_book.sort(key=lambda x: len(x))
answer = True

for i in range(len(phone_book)):
    for j in phone_book[i + 1:]:
        if j.startswith(phone_book[i]):
            answer = False
            break
    if answer == False:
        break

print(answer)

"""
def solution(phone_book):
    # 공백 제거 후 정렬
    phone_book = sorted([i.replace(" ", "") for i in phone_book])
    
    # 인접한 번호들만 비교
    for i in range(len(phone_book) - 1):
        # 접두사인지 확인
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True
    
    
    나 왜 길이로 정렬했지 그냥 정렬하면 접두사 후보들이 붙어있는데...
    2중 for문 -> 1중 for문
"""