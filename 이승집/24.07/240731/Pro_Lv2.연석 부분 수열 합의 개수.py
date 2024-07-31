elements = [7, 9, 1, 1, 4]
case = set()
l = len(elements)

"""
7 9 1 1 4

# 1. 길이가 1인 경우, 7, 9, 1, 1, 4

# 2. 길이가 2인 경우, 79, 91, 11, 14, 47

# 3. 길이가 3인 경우, 791, 911, 114, 147, 479

# 4. 길이가 4인 경우, 7911, 9114, 1147, 1479, 4791

# 5. 길이가 5인 경우 79114, 91147, 11479, 14791, 47911 

"""

for i in range(l):
    mid = elements[i]
    case.add(mid)
    for j in range(i+1, i+l):
        mid += elements[j%l]
        case.add(mid)

print(len(case))
