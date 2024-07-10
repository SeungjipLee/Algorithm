dart_result = "1D2S3T*"
star_star = {"S": 1, "D": 2, "T": 3}
divide_standard = "123"
answer_list = []
mid = ""

for i in dart_result:
    if i in divide_standard:
        answer_list.append(mid)
        mid = ""
    mid += i
answer_list.append(mid)
answer_list = answer_list[1:]
# print(answer_list)

num_list = [0] * len(answer_list)

for i in range(len(answer_list)):
    if "10" in answer_list[i]:
        num_list[i] = 10 ** star_star[answer_list[i][2]]
    else:
        num_list[i] = int(answer_list[i][0]) ** star_star[answer_list[i][1]]
    if len(answer_list[i]) >= 3:
        if answer_list[i][-1] == "*":
            num_list[i] *= 2
            if i != 0:
                num_list[i-1] *= 2
        elif answer_list[i][-1] == "#":
            num_list[i] *= (-1)


# print(num_list)
print(sum(num_list))
