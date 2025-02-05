def main():

    def find_self_number(n):
        ans = n
        while n != 0:
            ans += n % 10
            n //= 10
        return ans

    arr = list(range(1, 10001))
    for i in range(1, 10001):
        mid = find_self_number(i)
        if mid <= 10000 and mid in arr:
            arr.remove(mid)

    for i in arr:
        print(i)


if __name__ == '__main__':
    main()