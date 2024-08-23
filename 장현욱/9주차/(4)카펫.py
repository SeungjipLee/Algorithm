def solution(brown, yellow):
    answer = []
       
    for i in range(1,yellow+1):
    	#yellow의 약수를 이용해 row를 더 길게 설정한다.
        if(yellow % i ==0):
            yellow_row = (yellow / i) # 노란색의 가로
            yellow_col = i # 노란색의 높이
            if (2 * (yellow_row + yellow_col) + 4 == brown):
                return [yellow_row +2, yellow_col+2]