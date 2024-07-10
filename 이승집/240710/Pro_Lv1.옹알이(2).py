babbling = ["aya", "yee", "u", "maa"]
baby = ["aya", "ye", "woo", "ma"]

cnt = 0

for word in babbling:
    mid = ''
    left = word
    recent_word = ""
    for i in range(len(word)):
        mid += word[i]
        if mid in baby and mid != recent_word:
            left = left.replace(mid, "", 1)
            recent_word = mid
            mid = ""
    if not left:
        cnt += 1

print(cnt)