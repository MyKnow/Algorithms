# [string] word : 알파벳 대소문자로 이루어진 단어 (길이: < 1,000,000)
word = input()

# [string] upperWord : 알파벳 대문자로만 이루어진 word
upperWord = word.upper()

# [dict{string : int}] alphabetDict : upperWord에서 발견된 alphabet과 발견된 횟수를 저장하는 사전
alphabetDict = {}

# upperWord 순회
for alphabet in upperWord:
    # 이미 alphabetDict에 해당 alphabet이 존재한다면 횟수 업데이트
    if (alphabet in alphabetDict) :
        alphabetDict[alphabet] = alphabetDict[alphabet]+1
    # 존재하지 않는다면 alphabetDict에 추가한다.
    else :
        alphabetDict[alphabet] = 1
    
# [list(string)] mostFoundedAlphabetList : 리스트 컴프리헨션을 이용하여 얻어낸, 최빈값에 해당하는 알파벳 리스트
mostFoundedAlphabetList = [k for k, v in alphabetDict.items() if max(alphabetDict.values()) == v]

# mostFoundedAlphabetList의 길이가 2 이상이면 ?를 출력한다.
print("?" if len(mostFoundedAlphabetList) > 1 else mostFoundedAlphabetList[0])