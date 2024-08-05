def solution(price, money, count):
    answer = -1
    charge = price
    now_price = 0
    
    for i in range(1, count+1):
        print(price)
        now_price += price
        price += charge
        
    now_price = money - now_price
    print(now_price)
    if now_price < 0 :
        now_price *= -1
    
    else:
        now_price = 0

    return now_price