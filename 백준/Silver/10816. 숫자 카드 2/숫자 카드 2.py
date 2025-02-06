import sys

input = sys.stdin.readline

# [int] N: 상근이가 가지고 있는 숫자 카드의 개수 (범위(자연수): 1 ≤ N ≤ 500,000)
N = int(input())

# [dict(number: number)] dictOfCards: 상근이가 가지고 있는 카드를 저장하는 사전 (크기: N)
dictOfCards = dict()
for number in map(int, input().split()) :
    # 1. dictOfCards에 저장되지 않은 카드인 경우
    if (number not in dictOfCards):
        dictOfCards[number] = 1
    # 2. 저장된 카드인 경우
    else :
        # 카드 개수를 1 증가시킨다.
        dictOfCards[number] += 1

# [int] M: 입력될 정수의 개수 (범위(자연수): 1 ≤ M ≤ 500,000)
M = int(input())

for number in map(int, input().split()):
    if (number in dictOfCards.keys()):
        print(dictOfCards[number], end = " ")
    else :
        print(0, end = " ")