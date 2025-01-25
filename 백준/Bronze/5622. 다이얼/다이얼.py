# [string] word : 알파벳 대문자로 이루어진 단어 (길이: 2 <= len <= 15)
word = input()

# [int] sumOfTime : 다이얼을 돌린 총 시간
sumOfTime = 0

# [int] minTimeForInput : 다이얼을 돌리는 데 필요한 최소 시간
minTimeForInput = 2

# 문자열을 순회하며 소요되는 시간을 모두 합한다.
for alphabet in word :
    # [int] alphabetInAscii : 아스키코드에서의 alphabet
    alphabetInAscii = ord(alphabet)
    
    # 7번, 9번 다이얼은 알파벳이 4개 들어있으므로, 이를 처리하는 조건문을 생성함.
    if (alphabetInAscii < ord('P')) :
        # 알파벳 인덱스 차이에서 3을 나눈 몫을 최소 소요 시간과 더한 값을 이용한다.
        sumOfTime += minTimeForInput + 1 + (alphabetInAscii - ord('A')) // 3
    elif (alphabetInAscii <= ord('S')) :
        # P, Q, R, S 중 하나이므로 고정된 값을 더한다.
        sumOfTime += minTimeForInput + 6
    elif (alphabetInAscii < ord('W')) :
        # T, U, V 중 하나이므로 고정된 값을 더한다.
        sumOfTime += minTimeForInput + 7
    else :
        # W, X, Y, Z 중 하나이므로 고정된 값을 더한다.
        sumOfTime += minTimeForInput + 8
        
# sumOfTime 출력
print(sumOfTime)