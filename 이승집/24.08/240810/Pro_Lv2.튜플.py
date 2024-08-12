s = "{{20,111},{111}}"

li = s[1:-1]
print(li)

ans = []
mid = ""
for i in li:
    if i == "}":
        ans.append(set(mid.split(",")))
    elif i in "{":
        mid = ""
    else:
        mid += i

print(ans)

ans.sort(key= lambda x : len(x), reverse= True)
print(ans)

answer = []
for i in range(len(ans) - 1):
    answer.append((ans[i] - ans[i+1]).pop())
answer.append(ans[-1].pop())
answer.reverse()

answer = [int(i) for i in answer]
print(answer)