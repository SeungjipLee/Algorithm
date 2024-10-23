def solution(phone_book):
    d = {i : True for i in phone_book}
    
    for phone_num in phone_book:
        tmp = ""
        for num in phone_num[:-1]:
            tmp += num
            if d.get(tmp) != None:
                return False
    return True