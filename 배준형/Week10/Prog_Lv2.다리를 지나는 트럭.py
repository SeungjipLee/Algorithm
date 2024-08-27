import heapq
def solution(bridge_length, weight, truck_weights):
    answer = 0
    h = []
    i = 0
    time = 0
    cur_w = 0
    
    while True:
        time += 1
        
        if h and h[0][0] == time:
            t, wei = heapq.heappop(h)
            cur_w -= wei

        
        if i < len(truck_weights) and cur_w + truck_weights[i] <= weight:
            w = truck_weights[i]
            heapq.heappush(h, [time+bridge_length, w])
            cur_w += w
            i += 1

        if i == len(truck_weights) and not h:
            break        
        
    return time