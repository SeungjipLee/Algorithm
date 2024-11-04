n = int(input())
seats = input()
print(min(n, seats.count('S') + seats.count('L')//2 + 1))