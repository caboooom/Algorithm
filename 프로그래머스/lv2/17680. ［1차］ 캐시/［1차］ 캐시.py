def solution(cacheSize, cities): 
    # 실행시간 측정 프로그램 작성하기
    
    # hit -> 1,  miss -> 5
    # LRU
    if cacheSize == 0:
        return 5 * len(cities)
    
    time = 0
    cache = []
    for city in cities:
        city = city.lower() # 각 도시 이름은 대소문자 구분을 하지 않는다.
        if city in cache: # hit
            time += 1
            cache.remove(city)
            cache.append(city)
        else: # miss
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)

    return time