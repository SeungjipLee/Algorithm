r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

def r_cal(A):
    max_col_len = len(A[0])
    for i in range(len(A)):
        num_cnt_dict = {}
        for j in A[i]:
            if j == 0:
                continue

            num_cnt_dict[j] = num_cnt_dict.get(j, 0) + 1
        
        num_cnt_dict = dict(sorted(num_cnt_dict.items(), key=lambda item : (item[1], item[0])))
        new_ls = []
        for k, v in num_cnt_dict.items():
            new_ls.append(k)
            new_ls.append(v)

        A[i] = new_ls
        max_col_len = max(max_col_len, len(new_ls))

    for j in range(len(A)):
        add_zero_cnt = max_col_len - len(A[j])
        zero = [0] * add_zero_cnt
        A[j].extend(zero)
            

    return A


def c_cal(A):
    max_row_len = 0
    col_len = len(A[0])
    
    new_cols = []
    for i in range(col_len):
        num_cnt_dict = {}
        for j in range(len(A)):
            if A[j][i] == 0:
                continue

            num_cnt_dict[A[j][i]] = num_cnt_dict.get(A[j][i], 0) + 1
        
        num_cnt_dict = dict(sorted(num_cnt_dict.items(), key=lambda item : (item[1], item[0])))
        new_ls = []
        for k, v in num_cnt_dict.items():
            new_ls.append(k)
            new_ls.append(v)

        max_row_len = max(max_row_len, len(new_ls))
        new_cols.append(new_ls)

    for j in range(len(new_cols)):
        new_cols[i].extend([0] * (max_row_len - len(new_cols[i])))
        

    new_A = [[0] * col_len for _ in range(max_row_len)]
    for i in range(col_len):
        for j in range(len(new_cols[i])):
            new_A[j][i] = new_cols[i][j]


    return new_A


time = 0
while time <= 100:
    if arr[r-1][c-1] == k:
        break
    time += 1
    if len(arr) >= len(arr[0]):
        arr = r_cal(arr)
    else:
        arr = c_cal(arr)


if arr[r-1][c-1] == k:
    print(time)
else:
    print(-1)