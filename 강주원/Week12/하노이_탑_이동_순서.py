n = int(input())

def sol(n, start, end):
    if n == 1:
        print(start, end)
        return

    sol(n-1, start, 6-start-end)
    print(start, end)
    sol(n-1, 6-start-end, end)

print(2**n-1)
sol(n, 1, 3)