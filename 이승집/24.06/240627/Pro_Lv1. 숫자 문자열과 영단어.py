s = "one4seveneight"

numbers = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

# 48~57: 숫자, 97~122: 영어
# print(ord("0"))
# print(ord("9"))
# print(ord("a"))
# print(ord("z"))

answer = ""
mid = ""

for i in s:
    if 97 <= ord(i) <= 122:
        mid += i
        if mid in numbers:
            answer += numbers[mid]
            mid = ""
        continue

    if 48 <= ord(i) <= 57:
        answer += i

print(int(answer))