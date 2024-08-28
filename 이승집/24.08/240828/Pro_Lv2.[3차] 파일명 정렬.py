files = ["O00321", "O49qcGPHuRLR5FEfoO00321"]
answer = []

new = []
for i in range(len(files)):
    mid = ""
    num = ""
    k = 0
    while not files[i][k].isdecimal():
        mid += files[i][k]
        k += 1
    while files[i][k].isdecimal():
        num += files[i][k]
        k += 1
        if k == len(files[i]):
            break
    new.append((mid.lower(), int(num), i))

new.sort()

for i in new:
    answer.append(files[i[2]])

print(answer)