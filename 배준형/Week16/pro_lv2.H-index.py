def solution(citations):
    answer = 0
    arr = [0] * 10010
    for c in citations:
        if c == 0:
            continue
        arr[0] += 1
        arr[c+1] -= 1
        
    for i in range(10001):
        arr[i] += arr[i-1]

    for i in range(1000, -1, -1):
        if arr[i] >= i:
            return i
    else:
        return 0