def solution(cacheSize, cities):
    answer = 0

    cache = []

    for city in cities:
        city = city.lower()
        if not city in cache:
            if len(cache) < cacheSize:
                cache.append(city)
                answer += 5
            else:
                try:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
                except IndexError:
                    answer += 5
                    continue

        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1

    return answer