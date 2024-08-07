# 휴대폰의 자판은 컴퓨터 키보드 자판과는 다르게 하나의 키에 여러 개의 문자가 할당될 수 있습니다. 
# 키 하나에 여러 문자가 할당된 경우, 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀝니다.

# 예를 들어, 1번 키에 "A", "B", "C" 순서대로 문자가 할당되어 있다면 1번 키를 한 번 누르면 "A", 두 번 누르면 "B", 세 번 누르면 "C"가 되는 식입니다.

# 같은 규칙을 적용해 아무렇게나 만든 휴대폰 자판이 있습니다. 
# 이 휴대폰 자판은 키의 개수가 1개부터 최대 100개까지 있을 수 있으며, 특정 키를 눌렀을 때 입력되는 문자들도 무작위로 배열되어 있습니다. 
# 또, 같은 문자가 자판 전체에 여러 번 할당된 경우도 있고, 키 하나에 같은 문자가 여러 번 할당된 경우도 있습니다. 
# 심지어 아예 할당되지 않은 경우도 있습니다. 따라서 몇몇 문자열은 작성할 수 없을 수도 있습니다.

# 이 휴대폰 자판을 이용해 특정 문자열을 작성할 때, 키를 최소 몇 번 눌러야 그 문자열을 작성할 수 있는지 알아보고자 합니다.

# 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap과 입력하려는 문자열들이 담긴 문자열 배열 targets가 주어질 때, 
# 각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return 하는 solution 함수를 완성해 주세요.

# 단, 목표 문자열을 작성할 수 없을 때는 -1을 저장합니다.

def solution(keymap, targets):
    answer = []

    for word in targets:    # targets에 있는 한 단어에 대해서
        times = 0           # 누른 키 총합
        
        for char in word:   # 한 단어의 개별 문자에 대해
            flag = False    # 목표 문자열을 작성할수 있는지 없는지 판단하기 위함
            time = 101      # keymap의 원소의 길이가 최대 100이기 때문에 101로 설정
            # keymap에 있는 모든 원소를 반복하면서 가장 적게 누를수 있는 char(문자)를 찾음
            for key in keymap:      
                if char in key:	# key(문자열)안에 char(문자)가 존재하면
                    time = min(key.index(char)+1, time)
                    flag = True    # 목표 문자열을 작성할 수 있음
                    
            if not flag:           # 만약 keymap을 전부다 돌았는데도 문자를 찾지 못하면
                times = -1;break   # 목표 문자열을 작성할 수 없음 
            
            times += time          # 하나의 문자에 대해 누른 키를 총합(키)에 더해줌
            
        answer.append(times)        
        # targets에 있는 하나의 단어에 대해 수행이 끝났으면 answer에 누른 키 총합을 넣어줌
    
    return answer


# 2안
def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer