s = "abracadabra"
cnt = 0
temp = ""
mid = ""
tx = 0
ty = 0
li = []

for i in s:
    if mid == "":
        temp = i

    mid += i
    if temp == "" or i == temp:
        tx += 1
    else:
        ty += 1

    if tx == ty:
        li.append(mid)
        mid = ""
        tx = ty = 0
        temp = ""

if temp != "":
    li.append(mid)

print(li)
