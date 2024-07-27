s = "110010101001"

rotation = 0
remove_zero = 0

while s != "1":
    # 먼저 0 제거
    remove_zero += s.count("0")
    s = s.replace("0", "")

    binary = len(s)
    s = bin(binary)[2:]
    rotation += 1

answer = [rotation, remove_zero]
print(answer)