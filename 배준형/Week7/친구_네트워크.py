# 두 사람의 이름이 주어진다
# 두 사람이 친구가 되었다는 뜻이다
# 친구 관계인 사람은 건너건너 다 친구인 친구 네트워크에 속해 있다고 본다
# 두 사람에 의해 형성된 친구 네트워크에 몇 명이 있는지 출력하라
# A B 가 주어지면 우선 2명
# C D 가 주어지면 2명 (A, B 와 관련이 없으므로)
# A C 가 주어지면 AB 그룹과 CD 그룹이 이어지므로 4명이 된다

# 아이디어 1
# 간선 정보 저장해놓고 BFS 돌리고 추가되는 명수만큼 해당 이름에 숫자더하기
# 문제.. 100000명 있으면 100000명 정보를 업데이트 해야함...

# 필요한 로직
# 매번 친구 네트워크에 몇명이 있는지 알아야한다.
# 이름 두 개가 주어지면 두 친구가 어느 그룹에 속한지 알아야한다

# 이름으로 그룹을 조회할 수 있어야 한다
# 그룹은 현재 몇 명의 인원이 있는지 알아야 한다
# 둘 다 그룹이 없다면 그룹을형성
# 한쪽이 그룹이 없다면 그룹에 추가
# 둘 다 다른 그룹이라면 그룹을 병합

# 이것만 빠른 시간 내에 하면 풀 수 있음

# 연결리스트로 헤드를 옮겨서 그룹을 바꾸면
# 누가 어느 그룹인지 어떻게 조회?
# 이름 : 그룹 의 형태로 맵에 저장하게 되면 최악의 경우 n^2 시간복잡도로 그룹을 업데이트 해야하는게 아닌가

import sys
input_ = sys.stdin.readline

test_case = int(input_())
for test in range(test_case):
    num_of_connections = int(input_())
    group_num = 1
    name_group_map = {}
    num_of_members = {}
    changed_group = {}
    
    for connection in range(num_of_connections):  
        name1, name2 = input_().rstrip().split()
        group1 = name_group_map.get(name1)
        group2 = name_group_map.get(name2)
        if group1:
            while changed_group.get(group1):
                group1 = changed_group[group1]
        if group2:
            while changed_group.get(group2):
                group2 = changed_group[group2]
        
        if group1 == None and group2 == None:
            name_group_map[name1] = group_num
            name_group_map[name2] = group_num
            num_of_members[group_num] = 2
            print(num_of_members[group_num])    
            group_num += 1
            
        elif group1 and group2 == None:
            name_group_map[name2] = group1
            num_of_members[group1] += 1
            print(num_of_members[group1])   
             
        elif group2 and group1 == None:
            name_group_map[name1] = group2
            num_of_members[group2] += 1    
            print(num_of_members[group2])    
            
        else:
            if group1 != group2:
                changed_group[group2] = group1
                num_of_members[group1] += num_of_members[group2]
            print(num_of_members[group1])    
    