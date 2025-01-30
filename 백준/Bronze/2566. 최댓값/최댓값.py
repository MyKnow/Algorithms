# [tuple(int, int, int)] tupleOfMax : max값의 행, 열, 값을 저장하는 tuple
tupleOfMax = (-1, -1, -1)

for row in range(9):
    # [list(int)] rowOfMatrix: 매트릭스의 현재 row
    rowOfMatrix = list(map(int, input().split()))
    
    # rowOfMatrix를 순회하며 값 탐색
    for col in range(9):
        # tupleOfMax에 저장된 값보다 크면 현재 row, col, rowOfMatrix[col]을 저장
        if (rowOfMatrix[col] > tupleOfMax[2]):
            tupleOfMax = (row, col, rowOfMatrix[col])

print(tupleOfMax[2])
print(str(tupleOfMax[0]+1)+ " " + str(tupleOfMax[1]+1))