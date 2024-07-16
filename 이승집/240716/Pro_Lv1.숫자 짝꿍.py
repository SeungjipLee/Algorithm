X = "100"
Y = "203045"
Z = {i for i in X} & {i for i in Y}
print(Z)
cnt_dict = dict()
for i in Z:
    cnt_dict[i] = min(X.count(i), Y.count(i))

if not Z:
    print("-1")

if Z == {"0"}:
    print("0")

print(cnt_dict)
answer = []
for i in cnt_dict:
    for _ in range(cnt_dict[i]):
        answer.append(int(i))

answer.sort(reverse=True)
answer = [str(i) for i in answer]

ans = "".join(answer)
print(ans)