def solution(weights):
    answer = 0
    # 정렬
    sorted_weights = sorted(weights)
    # 중복 제거를 위해 set 사용
    set_weights = sorted(list(set(weights)))
    # 딕셔너리에 해당 몸무게를 가진 사람 수 카운트
    my_dict = {}
    for weight in sorted_weights:
        my_dict[weight] = my_dict.get(weight, 0) + 1
    
    # 시소로 비교 가능한 경우의 수는 4가지이다.
    # 같은 몸무게일 경우
    for weight in my_dict.values():
        # nC2만큼 값을 answer에 더해준다
        if weight > 1:
            answer += weight * (weight - 1) // 2

    # 나머지 3가지의 경우를 계산
    dists = [(4,3), (3,2), (4,2)]
    
    # 투포인터 형태로 순회
    for i in range(len(set_weights)-1):
        for j in range(i+1, len(set_weights)):
            left, right = set_weights[i], set_weights[j]

            # 최대 가능 배수인 2배를 넘어서면 break
            if left > right * 2:
                break

            # 가중치를 곱한 값이 일치하면 카운트
            for k in dists:
                total_left = left*k[0]
                total_right = right*k[1]
                if total_left == total_right:
                    answer += my_dict[left] * my_dict[right]
                    break

    return answer