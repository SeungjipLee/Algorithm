    s = input()
    s_length = len(s)
    for i in range(s_length):
        if s[i:] == s[i:][::-1]:
            print(s_length + i)
            break