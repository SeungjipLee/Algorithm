import math


def solution(w, h):
    new_w = w // math.gcd(w, h)
    new_h = h // math.gcd(w, h)

    first = 0
    d = new_w * new_h

    for i in range(1, new_w):
        first += int(h / w * i)

    return (math.gcd(w, h)) * (2 * first + (math.gcd(w, h) - 1) * d)