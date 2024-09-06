def solution(n, stations, w):
    answer = 0
    # 기존에 설치된 기지국 s, 전파 거리 w
    # s1-w ~ s1 ~ s1+w ~ s2-w ~ s2 ~ s2+w 
    # s1+w 와 s2-w 사이에 최소로 설치해야함
    s = 1
    e = 1
    for station in stations:
        e = station-w-1
        # print(s, e)
        # print(get_num_of_stations(s, e, w))
        answer += get_num_of_stations(s, e, w)
        s = station+w+1
    e = n
    answer += get_num_of_stations(s, e, w)    

    return answer

def get_num_of_stations(s, e, w):
    if s > e:
        return 0
    # print(s, e)
    if (e-s+1)%(2*w+1):
        return (e-s+1)//(2*w+1)+1
    return (e-s+1)//(2*w+1)