def SelectionSort(arr):
    for fill_slot in range(len(arr) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if arr[location] > arr[max_index]:
                max_index = location
            arr[fill_slot], arr[max_index] = arr[max_index], arr[fill_slot]
    return arr

my_list = [70, 15, 25, 19, 34, 44]

print(SelectionSort(my_list))