def solution(n):
    def backtrack(row, cols, diags1, diags2):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            diag1 = row - col
            diag2 = row + col
            if col not in cols and diag1 not in diags1 and diag2 not in diags2:
                count += backtrack(row + 1, cols | {col}, diags1 | {diag1}, diags2 | {diag2})
        return count

    return backtrack(0, set(), set(), set())
n = int(input())
print(solution(n))