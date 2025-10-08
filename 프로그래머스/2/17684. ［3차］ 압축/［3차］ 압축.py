# * LZW 압축
# 1. 길이가 1인 모든 단어 사전에 초기화
# 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾음
# 3. W에 해당하는 사전의 색인 번호를 출력, 이후 입력에서 w 제거
# 4. 입력에서 처리되지 않은 다음 글자 c가 남아있다면, w+c에 해당하는 단어를 사전에 등록
# 5. 2단계부터 다시 진행

from collections import deque

def solution(msg):
    # msg를 deque로 변환
    dq = deque(msg)
    
    # 1번 수행
    lzw = {chr(i+65): i+1 for i in range(26)}
    
    # last_idx: lzw의 마지막 색인 번호
    last_idx = 26
    
    # msg_len: 원본 메세지의 길이
    msg_len = len(msg)
    
    answer = []
    
    # 문자열 순회
    while dq:
        # 2, 3-2번 수행
        w = dq.popleft()
        while dq and w+dq[0] in lzw:
            w += dq.popleft()

        # 3-1번 수행
        answer.append(lzw[w])

        # 4번 수행
        if dq:
            last_idx += 1
            lzw[w+dq[0]] = last_idx
            
    return answer