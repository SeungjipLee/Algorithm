# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 
# 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 
# solution 함수를 작성해주세요.

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)  # 스코빌 리스트를 힙 선언 힙은 작은것 큰것 찾을때 유용

    if scoville[0] >= K:  # 스코빌의 가장 낮은 맵기가 K 이상이면 0을 반환
        return 0
    
    mixed = 0

    while len(scoville) != 1:
        i, j = heapq.heappop(scoville), heapq.heappop(scoville)  # 가장 작은 두개를 i와 j에 추가
        heapq.heappush(scoville, i + j*2)  # 나온 결과물을 다시 스코빌힙에 넣기
        mixed += 1
        if scoville[0] >= K:  # K 이상이 되면 break
            break
    
    if scoville[0] < K:  # 만약 기준치 이상의 맵기가 안만들어질 경우 -1을 반환
        return -1
    
    return mixed