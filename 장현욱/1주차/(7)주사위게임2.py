# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.


def solution(a, b, c, d):
    answer = 0
    nums = [a, b, c, d]
    nums_count = {x: nums.count(x) for x in nums}  # 겹치는 숫자가 몇개인지 확인
    # 4숫자 모두 같으면 1111*나온수
    if a == b == c == d:
        answer = 1111 * a
        return answer
    
    # 3숫자 같으면(10 * p + q)2
    if 3 in nums_count.values():
        p = max(nums_count, key=nums_count.get)
        q = min(nums_count, key=nums_count.get)
        return (10 * p + q) ** 2
    
    # 2,2숫자가 같으면(p + q) × |p - q|
    if len(nums_count) == 2 and all(value == 2 for value in nums_count.values()):
        p, q = nums_count.keys()
        return (p + q) * abs(p - q)
    # 2개만 같으면 같은p은 빼고 q * r
    elif len(set(nums)) == 3:
        p = [x for x in nums if nums.count(x) == 2][0]
        q, r = [x for x in nums if x != p]
        answer = q * r
    # 모두 다르면 가장 작은 숫자만큼 추가
    else:
        p = [a, b, c, d]
        p.sort()
        answer = p[0]
    return answer
