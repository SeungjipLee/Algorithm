m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
answer = []


def get_minutes(start, end):
    return (int(end[:2]) * 60 + int(end[3:])) - (int(start[:2]) * 60 + int(start[3:]))


def replace_sharps(s):
    s = s.replace('C#', 'c')
    s = s.replace('D#', 'd')
    s = s.replace('F#', 'f')
    s = s.replace('G#', 'g')
    s = s.replace('A#', 'a')
    s = s.replace('B#', 'b')
    return s


m = replace_sharps(m)

for idx, info in enumerate(musicinfos):
    s, e, title, word = info.split(",")
    word = replace_sharps(word)
    L = get_minutes(s, e)
    N = len(word)
    W = (word * (L // N + 1))[:L]

    if m in W:
        answer.append((L, -idx, title))

if answer:
    answer.sort(reverse=True)
    print(answer[0][2])
else:
    print("(None)")
