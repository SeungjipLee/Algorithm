s = "1 2 3 4"
arr = s.split()
arr = [int(i) for i in arr]
answer = ""
answer += f"{str(min(arr))} {str(max(arr))}"

print(answer)