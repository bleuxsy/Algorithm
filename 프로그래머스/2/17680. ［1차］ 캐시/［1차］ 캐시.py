from collections import deque
def solution(cacheSize, cities):
    answer = 0
    hit = 1
    miss = 5
    cache = deque()
    if cacheSize == 0 :
        return len(cities) * miss
    for i in range(len(cities)):
        city = cities[i].lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += hit
        else:
            if len(cache) >= cacheSize :
                cache.popleft()
                
            cache.append(city)
            answer += miss

    print(answer)
            
    return answer