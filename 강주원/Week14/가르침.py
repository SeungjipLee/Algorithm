import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
words = []

for i in range(n):
    # antic을 제외한 단어를 저장
    word = input().rstrip()[4:-4]
    new_word = ''
    for w in word:
        if w not in "antic":
            new_word += w
    words.append(new_word)


def sol():
    # 최소 5개의 글자를 배워야함
    if k < 5:
        return 0

    # 26개의 글자를 배우면 졸업
    if k == 26:
        return n

    # 비트마스킹한 단어를 저장
    word_bitmasks = []
    for word in words:
        bitmask = 0
        for ch in word:
            bitmask |= (1 << (ord(ch) - ord('a')))
        word_bitmasks.append(bitmask)

    available_chars = [chr(i+ord('a')) for i in range(26) if chr(i+ord('a')) not in "antic"]
    max_readable = 0
    for comb in combinations(available_chars, k-5):
        learn_mask = 0
        for c in comb:
            learn_mask |= (1 << (ord(c) - ord('a')))
        
        readable_count = 0
        for bitmask in word_bitmasks:
            if learn_mask & bitmask == bitmask:
                readable_count += 1

        max_readable = max(max_readable, readable_count)

    return max_readable

print(sol())