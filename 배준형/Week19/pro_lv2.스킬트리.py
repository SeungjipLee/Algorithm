def solution(skill, skill_trees):
    answer = 0
    n = len(skill)
    d = {}
    for idx, s in enumerate(skill):
        d[s] = idx + 1
    # print(d)
    for s_tree in skill_trees:
        skill_grade = 0
        for s in s_tree:
            # print(s)
            if d.get(s) == None:
                continue
            if skill_grade + 1 == d[s]:
                skill_grade += 1
                # print("스킬배움", skill_grade)
            else:
                # print("break at", s_tree, s)
                break
                
        else:
            answer += 1
    return answer