numbers = [8, 89, 887]

l = max([len(str(i)) for i in numbers])
mid = []

for i in range(len(numbers)):
    s = str(numbers[i])
    while len(s) < l:
        s += s[-1]
    mid.append((int(s), -i))

mid.sort(reverse=True)
print(mid)
print(numbers)
answer = ""
for i in mid:
    answer += str(numbers[-i[1]])

print(answer)

"""
-> import 부터 모르겠다 -> 숫자 범위가 1000이내이므로 *3을
한 다음에 sort를 때리면 된다고도 한다

from functools import cmp_to_key

def compare(x, y):
    # 두 문자열을 서로 이어붙였을 때 더 큰 쪽이 앞에 오도록 비교
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 비교 함수를 사용하여 정렬
    numbers.sort(key=cmp_to_key(compare))
    
    # 결과를 이어붙인 후 반환
    answer = ''.join(numbers)
    
    # 만약 결과가 '000'과 같은 경우가 있을 수 있으므로 '0'으로 변환
    return '0' if answer[0] == '0' else answer
"""