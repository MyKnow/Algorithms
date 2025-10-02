from collections import defaultdict

def getValue(s, c):
    if c < 4:
        return (s[0], 4-c)
    elif c > 4:
        return (s[1], c-4)
    else:
        return None
        

def solution(survey, choices):
    answer = ''
    
    d = defaultdict(int)
    
    for s, c in zip(survey, choices):
        result = getValue(s, c)
        print(result)
        
        if result is not None:
            d[result[0]] += result[1]
    
    for f, s in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        if d[f] >= d[s]:
            answer += f
        else:
            answer += s
        
    return answer