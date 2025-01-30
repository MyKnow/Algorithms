# [list(list(int))] matrix: 주어진 글자들을 저장하는 2차원 list
matrix = []

# 세로 길이는 5 고정
for row in range(5) :
    # [list] columnList: 영어 대소문자, 숫자로 구성된 문자열 (길이: 1 <= len <= 15)
    columnList = list(input())
    
    # 길이 15까지 *을 빈 자리에 채움
    for _ in range(15-len(columnList)) :
        columnList.append("*")
        
    # 매트릭스에 columnList를 append함
    matrix.append(columnList)
    
# 이제 matrix는 15*5의 고정 길이 matrix가 됨.
# 가로 길이만큼 반복
for col in range(15) :
    # 세로 길이만큼 반복
    for row in range(5):
        # "*"이 아닌 문자를 출력함
        if (matrix[row][col] != "*") :
            print(matrix[row][col], end="")