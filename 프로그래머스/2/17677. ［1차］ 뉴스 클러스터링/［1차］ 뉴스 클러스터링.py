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

# 영문자만 존재하는 원소만 다중 집합에 추가한다.
# 편의를 위해 모든 영문자를 소문자로 치환한다.
def getMultisetFromString(s):
    return [s[i:i+2].lower() for i in range(len(s)-1) if s[i:i+2].isalpha()]

def solution(str1, str2):
    # 각 str을 저장할 다중 집합을 리스트로 구현
    set_1, set_2 = getMultisetFromString(str1), getMultisetFromString(str2)
            
    # 두 다중 집합의 합집합과 교집합을 구한다.
    # 합집합은 두 집합 중 원소 갯수가 더 많은 쪽의 수를 따라간다.(max(a, b))
    # 교집합은 두 집합 중 원소 갯수가 더 적은 쪽의 수를 따라간다.(min(a, b))
    # 하지만 Counter는 자체적으로 &, | 연산이 가능하다.
    cnt_1 = Counter(set_1)
    cnt_2 = Counter(set_2)
    union = cnt_1 | cnt_2
    inter = cnt_1 & cnt_2
    
    if not union:
        # division by zero 방지를 위한 예외처리
        return 65536
    return int( sum(inter.values()) / sum(union.values()) * 65536)