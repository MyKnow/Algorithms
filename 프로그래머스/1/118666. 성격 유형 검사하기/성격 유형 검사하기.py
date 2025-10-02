from collections import defaultdict

def solution(survey, choices):
    d = defaultdict(int)

    for s, c in zip(survey, choices):
        if c < 4:
            d[s[0]] += 4 - c
        elif c > 4:
            d[s[1]] += c - 4

    answer = ''
    for f, s in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        answer += f if d[f] >= d[s] else s

    return answer