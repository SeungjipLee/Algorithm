new_id = "abcdefghijklmn.p"
step1 = new_id.lower()

print(step1)

step2 = ""
for char in step1:
    if char not in ".-_1234567890abcdefghijklmnopqrstuvwxyz":
        continue
    else:
        step2 += char

print(step2)


while True:
    if ".." in step2:
        step2 = step2.replace("..", ".")
    else:
        break

step3 = step2

print(step3)

while True:
    if step3:
        if step3[0] == ".":
            step3 = step3[1:]
        else:
            if step3[-1] == ".":
                step3 = step3[:-1]
            else:
                break
    else:
        step3 = ""
        break

step4 = step3

print(step4)

if step4 == "":
    step5 = "a"
else:
    step5 = step4

print(step5)

if len(step5) >= 16:
    step6 = step5[:15]
else:
    step6 = step5

print(step6)

while True:
    if step6[0] == ".":
        step6 = step6[1:]
    else:
        if step6[-1] == ".":
            step6 = step6[:-1]
        else:
            break

print(step6)

if len(step6) <= 2:
    while len(step6) <= 2:
        step6 += step6[-1]

step7 = step6

print(step7)