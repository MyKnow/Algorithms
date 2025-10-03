# lines -> list(str): N(1 ≦ N ≦ 2,000)개의 로그 문자열 (S기준 오름차순 정렬됨)
    # S -> str: 고정 길이 "2016-09-15 hh:mm:ss.sss" 형식 (응답완료 시간)
    # T -> str: 최대 소수점 셋째 자리까지 기록하며 뒤에는 초 단위를 의미 (ex: 0.1s, 0.001 ≦ T ≦ 3.000)
    

# => 임의의 시작점부터 1초동안 찍힌 로그가 가장 많은 구간의 로그 개수를 출력하는 문제

def solution(lines):
    n = len(lines)
    
    lst = []
    
    for line in lines:
        date, time, T = line.split(" ")
        
        # 시간 계산의 용이성을 위해, 시간 포맷을 0.001s을 1로 계산한 int로 변환한다.
        # 예외처리를 위해 day까지 계산에 포함한다.
        s_time = time.split(":")
        d = 15 * 24 * 60 * 60 * 1000
        h = int(s_time[0]) * 60 * 60 * 1000
        m = int(s_time[1]) * 60 * 1000
        s = int(float(s_time[2]) * 1000)
        t_time = d + h + m + s
        
        lst.append( [t_time-int(float(T[:-1]) * 1000)+1, t_time] )
    
    # max_log: 가장 많은 수의 로그가 찍힌 구간의 로그 개수를 기록
    max_log = 0
    
    # 각 로그의 시작지점으로부터 1초 및 끝지점으로부터 1초 범위의 로그 개수를 세고
    # 각 범위에 포함된 로그 개수를 max_log와 비교하여 업데이트
    for s, e in lst:
        for t in [s, e]:
            inner_s, inner_e = t, t+999
            
            count = 0
            for st, en in lst:
                if st <= inner_e and en >= inner_s:
                    count += 1
            max_log = max(max_log, count)
            
    return max_log
                