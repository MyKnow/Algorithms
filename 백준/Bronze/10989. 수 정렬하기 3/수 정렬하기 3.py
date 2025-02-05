import sys

# [int] N: 입력 받을 수의 개수 (범위: 1 <= N <= 10,000,000)
N = int(sys.stdin.readline().strip())

# [dict(int, int)] dictOfNumbers: 1부터 10,000까지의 자연수의 개수를 저장하는 사전 (길이: N)
dictOfNumbers = dict()
                 
# N번 입력 받는다.
for _ in range(N):
    number = int(sys.stdin.readline().strip())
    
    # 사전에 number가 존재하는 지 확인한다.
    if (number in dictOfNumbers.keys()):
        # dictOfNumbers[number]의 count를 1 증가시킨다.
        dictOfNumbers[number] += 1
    # 사전에 number가 없다면, 새롭게 추가한다.
    else :
        dictOfNumbers[number] = 1
        
for index in range(1, 10000+1):
    if (index in dictOfNumbers.keys()):
        for count in range(dictOfNumbers[index]):
            print(index)