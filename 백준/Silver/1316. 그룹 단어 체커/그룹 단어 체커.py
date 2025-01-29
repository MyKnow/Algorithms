# [int] N : 단어의 개수 (1 <= N <= 100)
N = int(input())

# [int] count : 발견된 그룹 단어의 개수
count = 0

for _ in range(N) :
    # [list(string)] stackOfAlphabet : 입력된 단어의 알파벳을 순서대로 저장하는 스택
    stackOfAlphabet = []
    
    # [string] word : 알파벳 소문자로만 이루어진 입력한 단어 (길이: <= 100)
    word = input()
    
    for index in range(len(word)) :
        # [string] alphabetOfNowIndex : 현재 인덱스의 알파벳
        alphabetOfNowIndex = word[index]
        
        # 만약 스택 안에 해당 알파벳이 없다면 추가한다.
        if (alphabetOfNowIndex not in stackOfAlphabet) :
            stackOfAlphabet.append(alphabetOfNowIndex)
        # 스택 안에 해당 알파벳이 존재하는데, Top에 위치하지 않다면 그룹 단어가 아니다.
        elif (stackOfAlphabet[-1] != alphabetOfNowIndex) :
                break
                
        # 마지막 인덱스까지 검사했는데도 이상이 없다면 count를 증가한다.
        if (index == len(word)-1) :
            count += 1
                
# count 출력
print(count)