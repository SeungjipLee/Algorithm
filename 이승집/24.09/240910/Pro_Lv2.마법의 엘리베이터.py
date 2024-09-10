def solution(storey):
    count = 0
    while storey > 0:
        digit = storey % 10  # 현재 자리의 숫자
        next_digit = (storey // 10) % 10  # 다음 자리의 숫자

        if digit > 5:
            # 10 - digit 만큼 버튼을 눌러 올림
            count += 10 - digit
            storey = (storey // 10) + 1  # 다음 자리로 이동하며 올림 처리
        elif digit == 5 and next_digit >= 5:
            # 다음 자리의 숫자가 5 이상이면 올림
            count += 5
            storey = (storey // 10) + 1
        else:
            # 현재 자리의 숫자만큼 버튼을 눌러 내림
            count += digit
            storey = storey // 10  # 다음 자리로 이동

    return count


print(solution(2324))