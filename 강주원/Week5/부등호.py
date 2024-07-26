n = int(input())
l = list(input().split())
ls = ['='] + [i for i in l if i != ' ']
temp = []

def sol(index, st):
    if index == n+1:
        temp.append(st)
        return

    for i in range(9, -1, -1):
        if index > 0:
            if ls[index] == '<':
                if int(st[-1]) < i and str(i) not in st:
                    st += str(i)
                    sol(index + 1, st)
                    st = st[:-1]
            else:
                if int(st[-1]) > i and str(i) not in st:
                    st += str(i)
                    sol(index + 1, st)
                    st = st[:-1]
        else:
            if str(i) not in st:
                st += str(i)
                sol(index + 1, st)
                st = st[:-1]


sol(0, '')
print(temp[0])
print(temp[-1])