def solution(s):
    words = []
    mid = ""
    for i in range(len(s)):
        if s[i] == " ":
            if mid != "":
                words.append(mid)
                mid = ""
            mid += " "
        else:
            if " " in mid:
                words.append(mid)
                mid = s[i]
            else:
                mid += s[i]
    if mid:
        words.append(mid)
    words = [word[0].upper() + word[1:].lower() for word in words]

    return "".join(words)