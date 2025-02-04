# [int] N: N번째 영화의 제목에 들어 갈 수 (범위(자연수): <= 10,000)
N = int(input())

# [int] nowNumber: 현재까지 찾은 조건에 부합한 수 (조건: 6이 3번 연속 들어간 수)
nowNumber = 666

# [int] count: 찾은 조건에 부합한 수의 개수
count = 0

while (True):
    listOfNumber = list(map(int, list(str(nowNumber))))
    
    # [int] countOfSix: 리스트 속 연속된 6의 개수
    countOfSix = 0
    for index in range(len(listOfNumber)):
        if (listOfNumber[index] == 6) :
            countOfSix += 1
        else :
            countOfSix = 0
            
        if (countOfSix == 3):
            count+=1
            break
    
    # N번째에 해당하는 수를 찾았다면 출력 및 종료
    if (count == N) :
        print(nowNumber)
        break
        
    nowNumber += 1