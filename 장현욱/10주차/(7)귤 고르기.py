# 경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 
# 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

# 예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 
# 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 
# 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

# 경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 
# 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.


def solution(k, tangerine):
    answer = 0
    apple_box = {} # 새로운 박스 딕셔너리 크기 : 갯수
    for i in tangerine: # 귤 크기를 하나씩 반복문 돌리기
        if i not in apple_box:  # 박스 안에 없다면 항목 추가
            apple_box[i] = 1
        else:
            apple_box[i] += 1
    
    apple_box_sorted = dict(sorted(apple_box.items(), key=lambda x:x[1], reverse = True))  # 벨류 값을 기준으로 오름차순 정렬 x[1]이 벨류값을 뜻함
    for i, j in apple_box_sorted.items():  # 딕셔너리 키와 벨류로 나눠서 반복문 사실 키값은 필요없음
        k -= j
        answer += 1
        if k < 1:
            break
        
            
    return answer