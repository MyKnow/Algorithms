from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    
    total = s1 + s2
    if total % 2 != 0:
        return -1
    
    target = total // 2

    limit = len(q1) * 3
    
    cnt = 0
    while cnt <= limit:
        if s1 == target:
            return cnt
        
        if s1 > s2:
            tmp = q1.popleft()
            s2 += tmp
            s1 -= tmp
            q2.append(tmp)
        else:
            tmp = q2.popleft()
            s1 += tmp
            s2 -= tmp
            q1.append(tmp)
        cnt+=1
        
    return -1