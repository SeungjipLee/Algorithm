st = input()
duck = "quack"
visit = [0] * len(st)
if len(st) % 5 :
    print(-1)
    exit()

def search(start):
    check = 0
    i = 0
    for s in range(start, len(st)):
        if st[s] == duck[i] and not visit[s]:
            if st[s] == 'k':
                check = 1

            visit[s] = 1
            i += 1
            i %= 5

    return check


res = 0
for i in range(len(visit)):
    if visit[i] == 0 and st[i] == 'q':
        check = search(i)
        if check:
            res += 1

if not res or not all(visit):
    res = -1
print(res)