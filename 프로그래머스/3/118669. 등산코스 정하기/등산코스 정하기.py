# 지점: 1~n까지 n개(각각 출입구, 쉼터, 산봉우리 중 하나)
# 양방향 통행이 가능한 등산로로 연결됨
# 쉼터 혹은 산봉우리를 방문할 때마다 휴식 가능
# 휴식없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 'intensity'라고 함.
#
# 출입구 중 한 곳에서 출발하여 산봉우리 중 한 곳만 방문한 뒤, 다시 '원래의 출입구'로 돌아와야 함
# => 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함.
#
# 해당 규칙을 지키며 intensity가 최소가 되도록 등산코스 정해야 함.
# => 가장 짧은 길만 선택하며 이동하는데, 산봉우리를 여러번 밟거나 다른 출입구를 밟으면 안됨.
#

from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    # 그래프 초기화
    graph = [[] for _ in range(n+1)]
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))
        
    # 산봉우리 집합
    summit_set = set(summits)
    
    # dist: 출발 지점에서 n지점까지의 최단거리
    dist = [10**18] * (n+1)
    hq = []
    
    # 다중 출발점 초기화
    for g in gates:
        dist[g] = 0
        heappush(hq, (0, g))
        
    while hq:
        # crt_cost: 해당 지점을 가는 시간
        # u: 지점 번호
        crt_cost, u = heappop(hq)
        
        # 1. 이미 최적의 경로가 존재하는 경우 확장 중단
        if crt_cost > dist[u]:
            continue
        
        # 2. 봉우리에 도착한 경우 확장 중단
        if u in summit_set:
            continue
            
        # 다음 경로 탐색
        for v, w in graph[u]:
            # crt_cost에 의해 이미 최단 시간은 정해짐
            next_cost = max(crt_cost, w)
            
            # 따라서 다음 경로가 최단 시간 이내로 통과 가능한 경우에만 확장
            if next_cost < dist[v]:
                dist[v] = next_cost
                heappush(hq, (next_cost, v))
                
    # intensity가 최소인 봉우리를 찾는다.
    summits_sorted = sorted(summits)
    best_s, best_int = 0, 10**18
    
    # 봉우리를 순회하며, 가장 intensity가 낮은 봉우리를 업데이트한다.
    for s in summits_sorted:
        if dist[s] < best_int:
            best_int = dist[s]
            best_s = s
            
    return [best_s, best_int]
            
        