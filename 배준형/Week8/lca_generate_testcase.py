import random

def generate_test_case(N, M):
    # 트리 생성
    print(N)
    edges = []
    for i in range(2, N+1):
        parent = random.randint(1, i-1)
        edges.append((parent, i))
    
    for edge in edges:
        print(edge[0], edge[1])

    # 쿼리 생성
    print(M)
    for _ in range(M):
        a = random.randint(1, N)
        b = random.randint(1, N)
        print(a, b)

# N(노드 수)와 M(쿼리 수)를 설정합니다.
N = 100  # 예시로 10을 사용
M = 50   # 예시로 5를 사용
generate_test_case(N, M)
