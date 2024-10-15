n = int(input())
bin_ = bin(n)
length = len(bin_)

res = 0
for i in range(len(bin_)-1, 1, -1):
    num = int(bin_[i])
    if not num:
        continue
    val_ = num * (length - i - 1)
    res += 3**val_

print(res)