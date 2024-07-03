def solution(answers):
    first = second = third = 0

    for i in range(1, len(answers) + 1):
        if i % 5 == (answers[i - 1]) % 5:
            first += 1
        if i % 2 and answers[i - 1] == 2:
            second += 1
        elif i % 2 == 0:
            if (i // 2) % 4 == 1 and answers[i - 1] == 1:
                second += 1
            elif (i // 2) % 4 == 2 and answers[i - 1] == 3:
                second += 1
            elif (i // 2) % 4 == 3 and answers[i - 1] == 4:
                second += 1
            elif (i // 2) % 4 == 0 and answers[i - 1] == 5:
                second += 1

        if (i % 10 == 1 or i % 10 == 2) and answers[i - 1] == 3:
            third += 1
        elif (i % 10 == 3 or i % 10 == 4) and answers[i - 1] == 1:
            third += 1
        elif (i % 10 == 5 or i % 10 == 6) and answers[i - 1] == 2:
            third += 1
        elif (i % 10 == 7 or i % 10 == 8) and answers[i - 1] == 4:
            third += 1
        elif (i % 10 == 9 or i % 10 == 0) and answers[i - 1] == 5:
            third += 1

    li = [(first, 1), (second, 2), (third, 3)]
    maximum = max(li)[0]
    answer = [i[1] for i in li if i[0] == maximum]

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
