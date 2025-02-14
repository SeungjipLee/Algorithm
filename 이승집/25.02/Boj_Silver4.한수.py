def main():
    n = int(input())
    def check(k):
        if k < 100:
            return True
        arr = []
        while k != 0:
            arr.append(k%10)
            k //= 10

        d = arr[0] - arr[1]
        for i in range(1, len(arr)-1):
            if arr[i] - arr[i+1] != d:
                return False
        return True

    ans = 0
    for i in range(1, n + 1):
        if check(i):
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()