arr = [100, 1, 2, 139, 51, 102]

maxi = mini = arr[0]
profit = 0

for i in arr[1:]:
    if i > mini:
        profit = max(profit, i - mini)
    mini = min(mini, i)

print(profit)