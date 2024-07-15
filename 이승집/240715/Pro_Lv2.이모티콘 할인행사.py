from itertools import product


users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
sales = [10, 20, 30, 40]
membership = 0
money = 0


for i in product(range(10, 50, 10), repeat=len(emoticons)):
    mid_membership = 0
    mid_money = 0

    for user in users:
        sum_money = 0

        for emoticon, sale in zip(emoticons, i):
            if sale >= user[0]:
                sum_money += emoticon * (100 - sale) // 100

        if sum_money >= user[1]:
            mid_membership += 1
        else:
            mid_money += sum_money

    if mid_membership > membership or (mid_membership == membership and mid_money > money):
        membership = mid_membership
        money = mid_money

print(membership, money)