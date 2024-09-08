ls = [int(input()) for _ in range(3)]
sum_val = sum(ls)
if sum_val != 180:
    print("Error")
elif ls[0] != ls[1] and ls[1] != ls[2] and ls[2] != ls[0]:
    print("Scalene")
elif ls[0] == ls[1] == ls[2]:
    print("Equilateral")
else:
    print("Isosceles")