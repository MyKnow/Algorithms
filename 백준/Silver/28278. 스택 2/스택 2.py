import sys

input = sys.stdin.readline

# [int] N: 명령의 수 (범위(자연수): 1 ≤ N ≤ 1,000,000)
N = int(input())

# [list(int)] stack: 정수를 저장할 스택
stack = list()

# [list(str)] listOfResult: 답을 저장하는 리스트
listOfResult = list()

for _ in range(N):
    order = input().strip()
    
    # 명령어가 1글자 초과인 경우, "1 X" 형태임.
    # 1. X를 스택에 넣기.
    if (len(order) > 1) :
        _, x = map(int, order.split())
        stack.append(str(x))
    # 2. 스택에 정수가 존재할 경우 빼고 출력한다.
    # 없다면 -1을 대신 출력한다.
    elif (int(order) == 2) :
        if (len(stack) > 0) :
            listOfResult.append(stack.pop())
        else :
            listOfResult.append("-1")
    # 3. 스택에 들어있는 정수의 개수를 출력한다.
    elif (int(order) == 3):
        listOfResult.append(str(len(stack)))
    # 4. 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif (int(order) == 4):
        if (len(stack) == 0):
            listOfResult.append("1")
        else :
            listOfResult.append("0")
    # 5. 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 출력한다.
    else:
        if (len(stack) > 0):
            listOfResult.append(str(stack[-1]))
        else:
            listOfResult.append("-1")
            
print("\n".join(listOfResult))