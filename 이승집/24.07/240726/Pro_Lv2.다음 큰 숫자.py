n = 15

binary = bin(n)[2:]
cnt = binary.count("1")

while True:
    n += 1
    if cnt == bin(n)[2:].count("1"):
        break

print(n)