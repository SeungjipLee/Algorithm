n = int(input())
def fibo(n):
    a,b = 1,1
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    for _ in range(1,n):
        a,b = b, a+b

    return a

print(fibo(n))