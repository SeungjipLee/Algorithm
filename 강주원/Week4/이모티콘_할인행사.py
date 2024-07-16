import itertools

def solution(users, emoticons):
    min_rate = min(users)[0]
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
    answer = res_ls[0]
    return answer
