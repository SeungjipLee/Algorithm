participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

cnt_dict = dict()
for i in participant:
    if i in cnt_dict:
        cnt_dict[i] += 1
    else:
        cnt_dict[i] = 1

for j in completion:
    cnt_dict[j] -= 1

for k in cnt_dict:
    if cnt_dict[k] == 1:
        print(k)
        break