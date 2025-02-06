import sys

input = sys.stdin.readline

# [int] T: 테스트 데이터의 개수 
T = int(input())

for _ in range(T):
    # [list(str)] listOfString: "("와 ")"로 구성된 문자열을 리스트로 변환함.
    listOfString = list(input().strip())
    
    # [list(str)] stack: "("와 ")"로 구성된 스택
    stack = []
    
    for p in listOfString :
        # 1. 여는 괄호를 만나면 스택에 넣는다.
        if (p == "("):
            stack.append(p)
        # 2. 닫는 괄호를 만나면 스택에서 뺀다.
        else :
            # 2-1. 만약, 스택이 비어있다면 올바른 문자열이 아니므로 바로 종료한다.
            if (len(stack) == 0):
                print("NO")
                break
            # 2-2. 스택에 괄호가 존재하면 제거한다.
            else :
                stack.pop()
    # break 없이 온전히 for문을 종료했을 때
    else:
        if (len(stack) == 0) :
            print("YES")
        else :
            print("NO")