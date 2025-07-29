# n: 각 집합의 길이
# s: 집합 속 각 원소의 총합
def solution(n, s):
    answer = []
    
    # s 나누기 n의 몫과 나머지를 구한다.
    div = s // n
    mod = s % n
    
    # 만약 몫이 0이면 집합을 생성할 수 없으므로, 요구조건에 따라 [-1]을 반환한다.
    if div == 0:
        return [-1]
    
    # 우선 answer 배열을 n개의 div 채운다.
    answer = [div for _ in range(n)]
    
    # 이후 answer 배열에서 mod개의 요소에 각각 1을 더한다.
    for idx in range(mod):
        answer[idx] += 1
        
    # 요구조건에 따라 오름차순 정렬하여 반환한다.
    return sorted(answer)
    