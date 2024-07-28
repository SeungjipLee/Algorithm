import math

N, A, B = 8, 4, 7

product = 1
while A != B:
    while A%(2**product) != 0:
        A += 1
    while B%(2**product) != 0:
        B += 1

    product += 1

print(product - 1)