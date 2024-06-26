def solution(sequence, k):
    l = len(sequence)
    seq_count = [0] * l
    seq_count[0] = sequence[0]
    
    possible_sum = {}
    
    for i in range(1, l):
        tmp_sum = seq_count[i-1] + sequence[i]
        possible_sum[tmp_sum] = i
        seq_count[i] = tmp_sum
    
    answer = []
    answer_l = 1e9
    
    for i in range(l):
        if sequence[i] == k:
            return [i, i]
        if seq_count[i] - k == 0 and i + 1 < answer_l:
            answer_l = i + 1     
            answer = [0, i]
        if possible_sum.get(seq_count[i]-k):
            idx = possible_sum[seq_count[i]-k]
            # print(i, idx, seq_count[i])
            if i - idx < answer_l:
                answer_l = i - idx
                answer = [idx+1 , i]
    return answer
