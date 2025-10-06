def getValueFromString(s):
    # 1. 입력되는 포맷이 "YYYY.MM.DD"이므로, .을 기준으로 나누고 int로 변환하여 반환한다.
    yyyy, mm, dd = map(int, s.split("."))
    yyyy = 28 * 12 * yyyy
    mm = 28 * mm
    return yyyy+ mm + dd
    
    

def solution(today, terms, privacies):
    answer = []
    
    transed_terms = dict()
    for term in terms:
        char, month = term.split()
        transed_terms[char] = int(month)
    
    for idx, privacy in enumerate(privacies):
        date, char = privacy.split()
        p_date = getValueFromString(date)
        
        addiction = transed_terms[char] * 28
        
        p_date += addiction
        
        
        t_date = getValueFromString(today)
        if t_date >= p_date:
            answer.append(idx+1)
            
    return answer

