n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

bin_arr1 = []
bin_arr2 = []

for i in arr1:
    bin_arr1.append(bin(i)[2:].zfill(n))

for i in arr2:
    bin_arr2.append(bin(i)[2:].zfill(n))

answer = []

for i in range(n):
    mid = ""
    for j in range(n):
        if bin_arr1[i][j] == '1' or bin_arr2[i][j] == '1':
            mid += "#"
        else:
            mid += " "
    answer.append(mid)

print(answer)