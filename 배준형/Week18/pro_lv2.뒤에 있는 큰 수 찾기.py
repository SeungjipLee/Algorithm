def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    big_idxs = [i for i in range(1, n+1)]
    big_idxs[-1] = -1
    
    for i in range(n-2, -1, -1):
        idx = i
        while True:
        # for e in range(10):
            if idx == -1:
                break
            if numbers[big_idxs[idx]] > numbers[i]:
                answer[i] = numbers[big_idxs[idx]]
                big_idxs[i] = big_idxs[idx]
                break
            idx = big_idxs[idx]
            if idx == n-1:
                big_idxs[i] = -1
                break
        # print(answer)
            
    return answer
