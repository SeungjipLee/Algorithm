def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(numbers)

    return '0' if answer[0] == '0' else answer