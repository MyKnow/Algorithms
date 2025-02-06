import sys

input = sys.stdin.readline

# [def(str) -> bool] isVPS: 문자열을 입력 받으면, VPS인지 판단하여 bool을 반환한다.
def isVPS(string):
    # [list(str)] listOfString: 문자열을 리스트로 변환함.
    listOfString = list(string)
    
    # [list(str)] stack: 문자열을 저장할 리스트
    stack = []
    
    for c in listOfString:
        # 1. 여는 괄호를 만나면 스택에 추가한다.
        if (c == "(" or c == "["):
            stack.append(c)
        # 2. 닫는 소괄호를 만나면, 조건을 검사한다.
        elif (c == ")"):
            # 2-1. 만약 스택이 비어있거나, 스택의 마지막이 여는 소괄호가 아니면 VPS가 아니다.
            if (len(stack) == 0 or stack[-1] != "("):
                return False
            # 2-2. 스택의 마지막이 여는 소괄호라면 제거한다.
            else :
                stack.pop()
        # 3. 닫는 대괄호를 만나면, 조건을 검사한다.
        elif (c == "]"):
            # 3-1. 만약 스택이 비어있거나, 스택의 마지막이 여는 대괄호가 아니면 VPS가 아니다.
            if (len(stack) == 0 or stack[-1] != "["):
                return False
            # 3-2. 스택의 마지막이 여는 대괄호라면 제거한다.
            else :
                stack.pop()
        # 4. 문장의 마지막인 온점을 만나면, 스택 상태를 확인한다.
        elif (c == "."):
            # 4-1. 스택의 길이를 확인하고, 비어있지 않다면 VPS가 아니다.
            if (len(stack) != 0) :
                return False
            else :
                return True

while(True):
    string = input().rstrip()
    
    if (string == "."):
        break
    else:
        print("yes" if isVPS(string) else "no")