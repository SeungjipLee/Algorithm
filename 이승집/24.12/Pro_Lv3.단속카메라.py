def solution(routes):
    answer = 0
    routes.sort(reverse=True)
    camera = 30001
    for route in routes:
        if camera > route[1]:
            answer += 1
            camera = route[0]
    return answer