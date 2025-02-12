def main():
    import sys
    input = sys.stdin.readline

    while True:
        numbers = list(map(int, input().split()))
        if numbers[0] == 0:
            break

        k = numbers.pop(0)



        def comb(numbers, start=0, path=[]):
            if len(path) == 6:
                print(*path)
                return

            for i in range(start, len(numbers)):
                comb(numbers, i + 1, path + [numbers[i]])

        comb(numbers)
        print()


if __name__ == '__main__':
    main()


"""input
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""

"""재귀로 구현한 combinations
def combinations(arr, r, start=0, path=[]):
    if len(path) == r:
        print(path)  # 조합 결과 출력 (혹은 리스트에 저장 가능)
        return
    
    for i in range(start, len(arr)):
        combinations(arr, r, i + 1, path + [arr[i]])  # 다음 원소 선택

# 예제 실행
arr = [1, 2, 3, 4]
r = 2
combinations(arr, r)
"""