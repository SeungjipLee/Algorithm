# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 
# 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 
# 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.


# 효율성 테스트 실패
def solution(people, limit):
    people.sort(reverse=True)  # 크기가 큰 수부터 작은순으로 숫자 리스트 정렬
    boat = 0

    while people:  # 사람이 남아있는동안 반복
        # 사람수가 1명 이상이고 제일 무거운 사람 + 가벼운사람이 한계점보다 낮거나 같을경우
        if len(people) > 1 and people[0] + people[-1] <= limit:
            boat += 1
            people.pop(0)
            people.pop()
        # 그 외의 경우
        else:
            boat += 1
            people.pop(0)
          
    return boat

# 효율성 보완 (포인터를 두고 리스트 조작x)
def solution(people, limit):
    people.sort()  # 몸무게를 오름차순으로 정렬
    i, j = 0, len(people) - 1  # 투 포인터 설정
    boat = 0

    while i <= j:
        boat += 1  # 항상 보트는 하나 사용
        if people[i] + people[j] <= limit:  # 가장 가벼운 사람과 가장 무거운 사람의 합이 제한 이하인 경우
            i += 1  # 가벼운 사람도 태움
        j -= 1  # 무거운 사람은 항상 태움

    return boat