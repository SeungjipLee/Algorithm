from collections import defaultdict
def solution(cacheSize, cities):
    answer = 0

    d = defaultdict(int)
    for idx, city in enumerate(cities):
        city = city.lower()
        
        if d[city] == 0:
            answer += 5
        else:
            answer += 1
            
        d[city] += 1
        
        if idx-cacheSize >= 0:
            d[cities[idx-cacheSize].lower()] -= 1

        
        
        
    return answer