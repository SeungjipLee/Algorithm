from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    on = deque([])
    truck = deque(truck_weights)
    S = 0
    while True:
        if not truck:
            if not on:
                return time
            else:
                while on:
                    if on[0][1] == time:
                        on.popleft()
                    time += 1
                return time

        if on and on[0][1] == time:
            S -= on.popleft()[0]

        if len(on) < bridge_length and S + truck[0] <= weight:
            mid = truck.popleft()
            S += mid
            on.append((mid, time + bridge_length))

        time += 1