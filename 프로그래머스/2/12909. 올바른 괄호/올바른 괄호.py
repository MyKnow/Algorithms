def solution(s):
    stack = 0
    for c in s:
        if c == "(":
            stack += 1
        else:
            if stack == 0:
                return False
            stack-=1
            
    if stack != 0:
        return False
    
    return True