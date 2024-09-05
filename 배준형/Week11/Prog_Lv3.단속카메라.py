def solution(routes):  
    routes.sort(key=lambda x: abs(x[1]-x[0]))
    c_routes = [[min(routes[0]), max(routes[0])]]

    for route in routes[1:]:
        x, y = min(route), max(route)
        for c_route in c_routes:
            a, b = c_route
            grouped = False
            if a <= x <= b:
                c_route[0] = x
                grouped= True
            if a <= y <= b:
                c_route[1] = y
                grouped= True
            if x <= a and b <= y:
                grouped = True
            if grouped:
                break         
        else:
            c_routes.append([x, y])
    # print(c_routes)
    return len(c_routes)

print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2