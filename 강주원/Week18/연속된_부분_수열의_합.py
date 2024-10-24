def solution(sequence, k):
    l, r = 0, 0
    sum_val = sequence[0]
    min_val = len(sequence)
    answer = [0, len(sequence)]
    while 1:
        if sum_val >= k:
            if sum_val == k and min_val > r-l:
                min_val = r-l
                answer = [l, r]
            sum_val -= sequence[l]
            l += 1
        else:
            r += 1
            if r == len(sequence):
                break
            sum_val += sequence[r]
            
            
    return answer
