# [list] listOfInt : 길이가 9로 고정된 서로 다른 자연수로 구성된 list
listOfInt = []

# 9번 반복하여 list에 int를 append
for _ in range(9) :
    listOfInt.append(int(input()))

# [int] maxOfList : list의 요소 중 최대값
maxOfList = max(listOfInt)

# [int] indexOfMax : max 값이 list에서 몇번째 인덱스인지 저장한 변수
indexOfMax = listOfInt.index(maxOfList)

print(maxOfList)
print(indexOfMax+1)
