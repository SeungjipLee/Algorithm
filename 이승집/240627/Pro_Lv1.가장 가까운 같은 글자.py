s = "foobar"

li = [-1] * 26

# 97, 122
print(ord("a"), ord("z"))

answer = []
for i in range(len(s)):
    if li[ord(s[i])-97] == -1:
        answer.append(-1)
    else:
        answer.append(i - li[ord(s[i])-97])
    li[ord(s[i]) - 97] = i

print(answer)