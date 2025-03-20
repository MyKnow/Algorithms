n = int(input())
listOfSequence = list(map(int, input().split()))

def solution():
    maxSum = listOfSequence[0]
    currentSum = listOfSequence[0]

    for i in range(1, n):
        currentSum = max(listOfSequence[i], currentSum + listOfSequence[i])
        maxSum = max(maxSum, currentSum)

    print(maxSum)

solution()