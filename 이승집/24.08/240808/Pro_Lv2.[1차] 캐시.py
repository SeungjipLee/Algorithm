cacheSize = 0
cities = ["Jeju", "Jeju"]

cities = [i.lower() for i in cities]
answer = 0
cache = [None] * cacheSize

for i in range(len(cities)):
    if cities[i] in cache:
        cache.remove(cities[i])
        cache = [cities[i]] + cache
        answer += 1
    else:
        if cacheSize != 0:
            cache = [cities[i]] + cache[:cacheSize-1]
        answer += 5

print(answer)

"""
제주
판교 제주
서울 판교 제주
뉴욕 서울 판교
LA 뉴욕 서울
제주 LA 뉴욕
판교 제주 LA
서울 판교 제주
뉴욕 서울 판교
LA 뉴욕 서울

50
---------

제주 - 5
판교 제주 - 5
서울 판교 제주 - 5
제주 서울 판교 - 1
판교 제주 서울 - 1
서울 판교 제주 - 1
제주 서울 판교 - 1
판교 제주 서울 - 1
서울 판교 제주 - 1

"""