# * 요약
# - 파일명에 포함된 숫자를 반영한 정렬 기능

# * 입력
# - files: HEAD, NUMBER, TAIL로 구성된 파일명을 포함하는 문자열 배열 (1,000개 이하)
#   - 구성
#       - HEAD: 숫자가 아닌 문자로 이루어져 있으며, 최소 한 글자 이상
#       - NUMBER: 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0 패딩이 올 수 있다.
#       - TAIL: HEAD, NUMBER를 제외한 나머지 부분
#           - 숫자가 다시 나타날 수도 있다.
#           - TAIL 부분이 없을 수도 있다.
#   - 각 파일명은 영문 대소문자, 숫자, 공백, ".", "-"만으로 이루어져있다. (100글자 이하)
#       -  영문자로 시작하며 숫자를 하나 이상 포함하고 있다.
#   - 중복된 파일명은 없으나, 대소문자나 숫자 앞부분의 0 차이가 있는 경우는 함께 주어질 수 있다.
#       - ex) "muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT" 가 함께 주어질 수 있음

# * 출력
# - 1. HEAD, 2. NUMBER, 3. 입력 순서의 우선순위로 오름차순 정렬된 파일명 리스트

# * 설계
# 1. files를 index로 순회하며 각 file을 얻는다.
#   1-1. 정규표현식을 이용해어 file을 head, number, tail로 나눈다.
#   1-2. head, number, index를 튜플로 묶어 list(answer)에  저장한다.
# 2. head, number, index 순서대로 정렬한 answer를 반환한다.

from re import compile, match

def solution(files):
    
    # 정규표현식: (숫자가 아닌 문자 1자리 이상), (숫자 1자리 이상 5자리 이하)
    pattern = compile(r"(\D{1,})(\d{1,5})")
    
    # 1
    answer = []
    for index, file in enumerate(files):
        # 1-1
        matched = match(pattern, file)
        if matched:
            head, number = matched.groups()
            
            # 1-2
            answer.append( (head.lower(), int(number), index, file))
        
    # 2
    return [file[3] for file in sorted(answer, key=lambda x: (x[0], x[1], x[2]))]