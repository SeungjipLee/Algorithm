while 1:
    try:
        a, b, c = map(int, input().split())
        if c - b >= b - a:
            print(c-b-1)
        else:
            print(b-a-1)
    except:
        exit()