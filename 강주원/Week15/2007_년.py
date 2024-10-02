x, y = map(int, input().split())
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

res = y-1
for i in range(1, x):
    res += day[i]

print(week[res%7])