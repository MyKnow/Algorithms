# * 요약
# - DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정
# - 캐시 교체 알고리즘은 LRU
#   - LRU: 가장 오랫동안 참조되지 않은 캐시를 교체하는 알고리즘
#   - 이미 존재하는 캐시를 재참조할 때는, 해당 캐시를 후순위로 재배치함.  
# - hit: 1, miss: 5

# * 입력
# - cacheSize: 캐시 크기 (0 이상 30 이하의 정수)
# - cities: 처리 할 도시이름 배열 (길이 100,000 이하의 문자열 배열, 알파벳 only, 대소문자 구분 없음, 최대 20자)

# * 출력
# - 주어진 cacheSize의 LRU 알고리즘으로 cities를 순서대로 처리할 때 걸리는 총 실행시간

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    # cache: LRU 알고리즘이 적용된 DB 캐시
    cache = deque([])
    
    # 예외처리: 만약 cacheSize가 0이라면 반드시 miss로 처리되므로, cities의 길이에 5를 곱한 값을 반환한다.
    if cacheSize == 0:
        return len(cities) * 5

    
    # 1. cities를 순회하며 실행시간을 업데이트 한다.
    for city in cities:
        # 대소문자는 구분하지 않으므로, 모든 city 이름은 소문자로 통일한다.
        city = city.lower()
        
        # hit: 이미 cache 안에 해당 city가 존재한다면, 실행시간에 1을 더하고 우선순위를 재배치한다.
        if city in cache:
            answer += 1
            cache.remove(city)
        # miss: cache에 해당 city가 존재하지 않는다면, 실행시간에 5를 더하고 추가한다.
        else:
            answer += 5
            
            # 만약 cache가 꽉 찼다면, 가장 오래된 캐시를 삭제한다.
            if len(cache) >= cacheSize:
                cache.popleft()
                
        # cache에 현재 city를 추가한다.
        cache.append(city)
    
    return answer