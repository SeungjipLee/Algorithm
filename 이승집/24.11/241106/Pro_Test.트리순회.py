s = "HELLOPYTHON"
N = len(s)


def pre_order(n):
    if n >= N:
        return

    print(s[n])
    pre_order(2 * n + 1)
    pre_order(2 * n + 2)


pre_order(0)
print("--------------")


def mid_order(n):
    if n >= N:
        return

    mid_order(2 * n + 1)
    print(s[n])
    mid_order(2 * n + 2)


mid_order(0)
print("--------------")


def post_order(n):
    if n >= N:
        return

    post_order(2*n+1)
    post_order(2*n+2)
    print(s[n])


post_order(0)