def main():
    import sys
    input = sys.stdin.readline
    
    n, q = map(int, input().split())
    
    # 삭제 여부를 체크하기 위한 배열 (False: 아직 남아 있음)
    row_removed = [False] * n
    col_removed = [False] * n
    
    # 남아있는 행과 열의 개수 및 인덱스 합
    row_count = n
    col_count = n
    row_sum = n * (n - 1) // 2
    col_sum = n * (n - 1) // 2
    
    for _ in range(q):
        word, num = input().split()
        num = int(num) - 1  # 0-indexed 변환
        
        if word == "R":
            # 해당 행이 이미 삭제되었다면 0 출력
            if row_removed[num]:
                print(0)
                continue
            
            # 행 num의 합 계산
            # 합 = (num+2) * (col_count) + (col_sum)
            ans = (num + 2) * col_count + col_sum
            print(ans)
            
            # 행 num 삭제 처리
            row_removed[num] = True
            row_count -= 1
            row_sum -= num
            
        else:  # "C"인 경우
            if col_removed[num]:
                print(0)
                continue
            
            # 합 = (num+2) * (row_count) + (row_sum)
            ans = (num + 2) * row_count + row_sum
            print(ans)
            
            # 열 num 삭제 처리
            col_removed[num] = True
            col_count -= 1
            col_sum -= num

if __name__ == '__main__':
    main()
