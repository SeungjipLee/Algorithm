N = int(input())

A = list(map(int, input().split()))

indexed_A = list(enumerate(A))

sorted_A = sorted(indexed_A, key=lambda x: x[1])

P = [0] * N

for new_idx, (original_idx, value) in enumerate(sorted_A):
    P[original_idx] = new_idx

print(' '.join(map(str, P)))
