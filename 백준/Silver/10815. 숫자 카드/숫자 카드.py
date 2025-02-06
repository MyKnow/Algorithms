# [int] N: 상근이가 가지고 있는 숫자 카드의 개수 (범위(자연수): 1 ≤ N ≤ 500,000)
N = int(input())

# [dict(number: number)] dictOfCards: 상근이가 가지고 있는 카드를 저장하는 사전 (크기: N)
dictOfCards = dict()
for number in map(int, input().split()) :
    dictOfCards[number] = 1

# [int] M: 입력될 정수의 개수 (범위(자연수): 1 ≤ M ≤ 500,000)
M = int(input())

result = []
for number in map(int, input().split()):
    if (number in dictOfCards.keys()):
        result.append(1)
    else :
        result.append(0)
        
print(" ".join(map(str, result)))