x = int(input())
y = int(input())

# 두 숫자는 모두 양수 또는 음수로, 0을 제외한 절댓값 1000 이하의 정수다.
# 따라서 무조건 1~4분면에 속하므로, 조건의 수는 4개다.

if (y > 0) :
    if (x > 0) :
        print(1)
    else :
        print(2)
        
else :
    if (x < 0) :
        print(3)
    else :
        print(4)