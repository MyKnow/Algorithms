from collections import defaultdict

def solution(X, Y):
    answer = ''
    
    # X의 각 자리에 해당하는 수가 몇 번 등장하는 지 체크하는 Dictionary 생성
    dictOfX = defaultdict(int)
    
    # X를 순회하며 dictOfX를 업데이트한다.
    for strN in X:
        dictOfX[strN] += 1
    
    # Y를 순회하며 dictOfX에 존재하는 키값인 경우 answer에 append하고 dictOfX의 value를 감소시킨다.
    # dictOfX의 value가 0 이하인 경우, 사전에서 제거하여 answer에 추가되지 못하게 방지한다.
    for strN in Y:
        if strN in dictOfX:
            if dictOfX[strN] <= 0:
                dictOfX.pop(strN)
            else:
                answer += strN
                dictOfX[strN] -= 1
                
    # answer가 빈 문자열이라면 "-1"을 반환한다.
    if len(answer) == 0:
        return "-1"
    
    # answer가 0으로만 구성되어 있다면, 0만 반환한다.
    if set(answer) == {"0"}:
        return "0"
    
    # 내림차순 정렬한 뒤 str로 반환한다.
    return "".join(sorted(answer, reverse=True))