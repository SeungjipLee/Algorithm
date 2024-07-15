import string

keymap = ["AA"]
targets = ["B"]
answer = []

alphabet_dict = {letter: 100 for letter in string.ascii_uppercase}

print(alphabet_dict)

for i in keymap:
    for j in range(len(i)):
        k = i[j]
        if alphabet_dict[k] > j + 1:
            alphabet_dict[k] = j + 1

print(alphabet_dict)

for i in targets:
    mid = 0
    for j in i:
        if alphabet_dict[j] != 100:
            mid += alphabet_dict[j]
        else:
            mid = -1
            break
    answer.append(mid)

print(answer)