n = int(input())
seats = input()

cup_holder = seats.count('S') + seats.count('L')//2 + 1
print(min(n, seats.count('S') + seats.count('L')//2 + 1))