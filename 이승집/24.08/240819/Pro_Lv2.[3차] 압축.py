import time
from collections import deque

start = time.time()

save = {chr(i): i-64 for i in range(65, 91)}
idx = 27

msg = "TOBEORNOTTOBEORTOBEORNOT"
answer = []
Q = deque([True])

for i in range(len(msg)):
    if Q.popleft():
        j = 1
        while msg[i:i + j] in save and i + j <= len(msg):
            j += 1
            if i + j > len(msg):
                break
        Q += [False] * (j-2)
        Q += [True]
        answer.append(save[msg[i:i+j-1]])
        save[msg[i:i+j]] = idx
        print(msg[i:i+j], idx)
        idx += 1


print(answer)

end = time.time()
print(end - start)