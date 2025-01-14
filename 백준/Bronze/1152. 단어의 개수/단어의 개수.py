# [string] S : 영어 대소문자와 공백으로 이루어진 문자열 (길이: < 1,000,000)
S = input()

# [string] stringWithStrip : 양쪽 공백을 strip 함수를 통해 지운 S
stringWithStrip = S.strip()

# 만약 stringWithStrip의 결과가 빈 문자열이라면, 0으로 처리한다.
if (stringWithStrip == "") :
    print(0)
else :
    # 공백을 기준으로 문자열을 나누어 list에 넣고, 해당 list의 길이를 출력한다.
    # [list] listOfWords : 문자열에서 추출한 단어들을 담은 list
    listOfWords = stringWithStrip.split(' ')

    # list의 길이를 출력한다.
    print(len(listOfWords))