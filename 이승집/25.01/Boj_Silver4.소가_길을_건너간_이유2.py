# ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
data = input().strip()
# 각 소의 첫 번째와 두 번째 위치를 저장할 딕셔너리
positions = {}

# 소들의 위치 저장
for i, cow in enumerate(data):
    if cow not in positions:
        positions[cow] = [i]  # 첫 번째 위치 저장
    else:
        positions[cow].append(i)  # 두 번째 위치 저장

# 교차 횟수 계산
cross_count = 0
cows = list(positions.keys())

# 모든 소 쌍을 비교
for i in range(len(cows)):
    for j in range(i + 1, len(cows)):
        cow1, cow2 = cows[i], cows[j]
        # cow1과 cow2의 구간
        cow1_start, cow1_end = positions[cow1]
        cow2_start, cow2_end = positions[cow2]
        
        # 교차 여부 확인
        if (cow1_start < cow2_start < cow1_end < cow2_end) or (cow2_start < cow1_start < cow2_end < cow1_end):
            cross_count += 1

# 결과 출력
print(cross_count)
