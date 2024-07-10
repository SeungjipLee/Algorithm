def to_minute(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(book_time):
    answer = 0
    minutes = [0] * 1500
    
    for time in book_time:
        s, e = map(to_minute, time)
        for i in range(s, e+10):
            minutes[i] += 1
    
    answer = max(minutes)
        
    return answer