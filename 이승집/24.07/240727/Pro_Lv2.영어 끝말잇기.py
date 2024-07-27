n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]


def solution(n, words):
    turn = 1
    recent = words[0]
    past = [words[0]]

    while turn < len(words):
        now = words[turn]
        # 마지막 끝 글자와 동일한 지 확인
        if recent[-1] != now[0]:
            break

        # 중복이 아닌지 확인
        if now in past:
            break

        past.append(now)
        recent = now
        turn += 1

    if turn == len(words):
        answer = [0, 0]
    else:
        answer = [turn % n + 1, turn // n + 1]

    return answer