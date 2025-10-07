# 자카드 유사도: 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값(다중집합에서도 가능)

# * 입력
# - str1, str2: 유사도를 계산할 두 문자열
#   - 길이: 2 이상 1,000 이하
#   - 두 글자씩 끊어서 다중 집합의 원소로 만든다.
#       - ex) FRANCE -> {FR, RA, AN, NC, CE}
#   - 영문자로 된 글자쌍만 유효, 그 외는 해당 글자쌍을 버린다
#       - ex) ab+ -> ab, (b+ 버림)
#   - 대소문자 차이는 무시한다.
#
# * 출력
# - 두 문자열의 자카드 유사도 출력(0~1 사이의 실수이므로, 65,536을 곱한 후 정수부만 출력

from collections import Counter

def solution(str1, str2):
    div = 65_536
    
    # 각 str을 저장할 다중 집합을 리스트로 구현
    set_1, set_2 = [], []
    
    # 각 다중 집합 업데이트
    # 영문자만 존재하는 원소만 다중 집합에 추가한다.
    # 편의를 위해 모든 영문자를 소문자로 치환한다.
    for i in range(len(str1)-1):
        crt_word = str1[i:i+2]
        if crt_word.isalpha():
            set_1.append(crt_word.lower()) 
    for i in range(len(str2)-1):
        crt_word = str2[i:i+2]
        if crt_word.isalpha():
            set_2.append(crt_word.lower()) 
            
    # 두 다중 집합의 합집합과 교집합을 구한다.
    # 합집합은 두 집합 중 원소 갯수가 더 많은 쪽의 수를 따라간다.(max(a, b))
    # 교집합은 두 집합 중 원소 갯수가 더 적은 쪽의 수를 따라간다.(min(a, b))
    cnt_1 = Counter(set_1)
    cnt_2 = Counter(set_2)
    
    union = [max(cnt_1.get(x, 0), cnt_2.get(x, 0)) for x in set(cnt_1) | set(cnt_2)]
    inter = [min(cnt_1.get(x, 0), cnt_2.get(x, 0)) for x in set(cnt_1) & set(cnt_2)]
    
    if not union:
        return div
    
    
    return int(sum(inter)/sum(union)*65536)