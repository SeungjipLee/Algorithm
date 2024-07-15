import itertools
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
min_rate = min(users)[0]
emoticons = [1300, 1500, 1600, 4900]
discounts = []
for i in [10, 20, 30, 40]:
    if i >= min_rate:
        discounts.append(i)

combinations = list(itertools.product(discounts, repeat=len(emoticons)))

res_ls = []
for combination in combinations:
    temp = [0,0]
    
    for user in users:
        user_rate = user[0]
        
        user_balance = user[1]
        total = 0
        is_singup = 0
        for num in range(len(emoticons)):
            discount_rate = combination[num]
            if user_rate > discount_rate:
                continue
            emoticon = emoticons[num]
            price = (1-(discount_rate/100)) * emoticon
            total += price
        if total >= user_balance:
            temp[0] += 1
        else:
            temp[1] += int(total)

    res_ls.append(temp)

res_ls.sort(key=lambda x:(-x[0], -x[1]))
print(res_ls[0])