from collections import deque, defaultdict

def solution(gems):
    answer = []
    # 최대 10만개의 보석

    gem_map = defaultdict(int)
    n = len(gems)  # n : 배열 길이
    m = len(set(gems)) # m : 보석 종류
    
    q = deque()
    i, j = 0, 0
    while j < n:
        q.append(gems[j])
        gem_map[gems[j]] += 1
        if len(gem_map) == m:
            # 압축할 수 있는 만큼 압축하기
            while True:
                now = q.popleft()
                gem_map[now] -= 1
                if gem_map[now] == 0:
                    q.appendleft(now)
                    gem_map[now] += 1 
                    break
                i += 1
            answer.append([i+1, j+1])

        j += 1
            
    return sorted(answer, key=lambda x: (x[1]-x[0], x[0]))[0]