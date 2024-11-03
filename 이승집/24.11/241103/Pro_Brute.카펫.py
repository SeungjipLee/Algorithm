def solution(brown, yellow):
    """
    가로를 x, 세로를 y라 하면
    전체 x * y 중
    갈색 : 2x + 2y - 4
    노란 : 전체 - 2x - 2y + 4
    """
    s = brown + yellow
    h = w = 0
    for h in range(1, s + 1):
        if s % h == 0:
            w = s//h
            if brown == 2 * w + 2 * h - 4:
                break
    return [w, h]
