def solution(begin, target, words):
    # target이 words에 없으면 변환 불가능
    if target not in words:
        return 0

    # 모든 단어 리스트에 begin 추가
    words = words + [begin]
    word_len = len(begin)

    # 각 단어에 대해 한 글자만 다른 단어들을 찾기 위한 인접 리스트 생성
    adj = {word: [] for word in words}
    for word1 in words:
        for word2 in words:
            if word1 != word2 and sum(a != b for a, b in zip(word1, word2)) == 1:
                adj[word1].append(word2)
    print(adj)

    # BFS를 위한 큐와 방문 기록 세트 초기화
    stack = [(begin, 0)]
    visited = set([begin])

    while stack:
        current_word, steps = stack.pop(0)
        # target에 도달하면 변환 횟수 반환
        if current_word == target:
            return steps
        # 인접한 단어들에 대해 탐색
        for next_word in adj[current_word]:
            if next_word not in visited:
                visited.add(next_word)
                stack.append((next_word, steps + 1))

    # 변환 불가능하면 0 반환
    return 0
