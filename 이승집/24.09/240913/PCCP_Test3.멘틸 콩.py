def find_gene(x, y):
    # 1세대는 항상 Rr
    if x == 1:
        return "Rr"

    # 부모의 유전자를 재귀적으로 구함
    parent = find_gene(x - 1, (y + 3) // 4)

    # 부모가 Rr인 경우, y에 따라 자식의 유전자가 달라짐
    if parent == "Rr":
        if y % 4 == 1:
            return "RR"
        elif y % 4 == 2 or y % 4 == 3:
            return "Rr"
        else:
            return "rr"
    # 부모가 RR인 경우
    elif parent == "RR":
        return "RR"
    # 부모가 rr인 경우
    else:
        return "rr"

find_gene(7, 2001)