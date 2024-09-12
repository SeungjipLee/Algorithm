n = 38
ans = []
while n:
    mid = n % 3
    if not mid:
        mid = 3
        n -= 1
    ans.append(str(mid))
    n //= 3

answer = "".join(ans[::-1])
answer = answer.replace("3", "4")

print(answer)