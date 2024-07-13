s = "yyyyy"
skip = "za"
index = 2
result = ""
ban = []

# 97 ~ 122
for i in skip:
    ban.append(ord(i))

for i in s:
    j = ord(i)
    for k in range(index):
        j = ((j + 1) - 97)%26 + 97
        while j in ban:
            j = ((j + 1) - 97)%26 + 97
    result += chr(j)

print(result)