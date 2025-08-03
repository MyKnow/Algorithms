# 질문하기 눌렀다가 "이분탐색"임을 스포당해버렸다.
#
# 어째서 이분탐색인가? :
# 정답을 찾으려면 “시간 T 안에 요구량을 채울 수 있는가?”라는 판단 문제로 바꾸는 게 핵심이다.
# 그 판단이 T가 커질수록 참이 되면, 작아질수록 거짓이 되는 단조성(Monotonic)을 갖기 때문에
# 그 경계(최소 T)를 찾는 데 이분탐색이 들어간다.
#
# 최적의(빠른) 시간을 찾는 게 목표인데, 어째서 커질 수록 참인가? :
# T가 크면 → 트럭들이 더 오래 움직일 수 있음 → 왕복을 더 많이 함 → 더 많은 금과 은을 옮김.
# T가 작으면 → 트럭들이 움직일 시간이 부족함 → 왕복 횟수가 적음 → 옮길 수 있는 금·은이 줄어듦.

def solution(a, b, g, s, w, t):
    low = 0
    high = 10**15
    cntOfCity = len(g)

    while low < high:
        mid = (low + high) // 2
        
        sumGold = 0
        sumSilver = 0
        sumTotal = 0
        
        for i in range(cntOfCity):
            full = mid // (2 * t[i])
            rem = mid % (2 * t[i])
            if rem >= t[i]:
                full += 1
            capacity = full * w[i]
            
            sumGold += min(g[i], capacity)
            sumSilver += min(s[i], capacity)
            sumTotal += min(g[i] + s[i], capacity)
        
        if sumGold >= a and sumSilver >= b and sumTotal >= a + b:
            high = mid
        else:
            low = mid + 1
    
    return low