from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

truck_weights.reverse()

answer = 0
now = 0
reservation = deque()

while truck_weights:
    if reservation and reservation[0][0] == answer:
        now -= reservation[0][1]
        reservation.popleft()

    if truck_weights[-1] + now <= weight:
        w = truck_weights.pop()
        now += w
        reservation.append((answer + bridge_length, w))

    answer += 1

print(answer+bridge_length)