my_list = [44, 16, 83, 7, 67, 21, 34, 45, 10]


def MergeSort(arr):
    if len(arr) > 1:
        # 리스트를 반으로 나눈다.
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # 나뉜 부분의 크기가 1이 될 때까지 반복한다.(여기서 재귀를 쓰기 때문에 함수형으로 정의함)
        MergeSort(left)
        MergeSort(right)

        a = b = c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                arr[c] = left[a]
                a += 1
            else:
                arr[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1

    return arr

print(MergeSort(my_list))