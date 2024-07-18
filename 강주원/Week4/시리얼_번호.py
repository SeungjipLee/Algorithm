import sys
input = sys.stdin.readline

n = int(input())
ls = []
my_dict = {}
for i in range(n):
    serial = input().rstrip()
    sum_val = 0
    for num in serial:
        if num.isdecimal():
            sum_val += int(num)

    temp = [serial, sum_val]
    ls.append(temp)

ls.sort(key = lambda x:(len(x[0]), x[1], x[0]))

for i in ls:
    print(i[0])
