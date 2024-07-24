s = "  s2   s3    s4     s5      "

word_arr = []
space_arr = []
answer = ""
mid = ""
space = ""

for i in s:
    if i == " ":
        if mid != "":
            word_arr.append(mid)
            mid = ""
        space += " "
    else:
        if space != "":
            space_arr.append(space)
            space = ""
        mid += i
if mid != "":
    word_arr.append(mid)
if space != "":
    space_arr.append(space)

if len(word_arr) < len(space_arr):
    word_arr.append("")
elif len(word_arr) > len(space_arr):
    space_arr.append("")


if s[0] == " ":
    for i in range(len(word_arr)):
        answer += space_arr[i]
        answer += word_arr[i]
else:
    for i in range(len(word_arr)):
        answer += word_arr[i]
        answer += space_arr[i]

print(answer)
print(s.title())