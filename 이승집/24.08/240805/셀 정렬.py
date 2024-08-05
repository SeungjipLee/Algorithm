def ShellSort(arr):
    distance = len(arr) // 2
    while distance > 0:
        for i in range(distance, len(arr)):
            temp = arr[i]
            j = i

            while j >= distance and arr[j-distance] > temp:
                arr[j] = arr[j-distance]
                j -= distance
            arr[j] = temp

        distance //= 2
    return arr


my_list = [10, 8 , 6, 20, 4, 3, 22, 1, 0 ,15, 16]
print(ShellSort(my_list))