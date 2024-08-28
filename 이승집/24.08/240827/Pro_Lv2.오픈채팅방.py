record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

id_name = dict()
for i in record:
    A = i.split()
    if len(A) == 3:
        id_name[A[1]] = A[2]

answer = []
for i in record:
    B = i.split()
    if len(B) == 2:
        answer.append(f'{id_name[B[1]]}님이 나갔습니다.')
    elif B[0] == "Change":
        continue
    else:
        answer.append(f'{id_name[B[1]]}님이 들어왔습니다.')

print(answer)