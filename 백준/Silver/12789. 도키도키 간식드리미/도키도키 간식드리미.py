# [int] N: 승환이 앞에 서 있는 학생들의 수 (범위(자연수): (1 ≤ N ≤ 1,000)
N = int(input())

# [list(int)] nowLine: 현재 승환이 앞에 서 있는 학생들의 줄을 의미하는 스택
nowLine = list(map(int, input().split()))[::-1]

# [list(int)] subLine: 한 명씩만 설 수 있는 예비 대기열 스택
subLine = list()

# [int] enterNumber: 현재 입장 가능한 번호 (초기값: 1)
enterNumber = 1

while(True):
    # 1. 먼저 현재 대기열에 사람이 있는 지 확인한다.
    if (len(nowLine) != 0):
        # 1-1. 현재 대기열에서 바로 입장할 수 있다면 스택에서 삭제하고, enterNumber를 1 증가시킨다.
        if (nowLine[-1] == enterNumber):
            nowLine.pop()
            enterNumber += 1
        # 1-2. 바로 입장할 수 없다면, 임시 대기열로 이동할 수 있는 지 확인한다.
        # 임시 대기열이 비어있거나, 임시 대기열의 최상단이 현재 대기열 최상단보다 높은 번호이어야 이동할 수 있다.
        elif (len(subLine) == 0 or nowLine[-1] < subLine[-1]):
            subLine.append(nowLine.pop())
        # 1-3. 현재 대기열에서 어떠한 이동도 불가능하다면, 임시 대기열에서 이동이 가능한 지 확인한다.
        elif (len(subLine) != 0):
            # 1-3-1. 임시 대기열에서 바로 입장할 수 있다면 스택에서 삭제하고, enterNumber를 1 증가시킨다.
            if (subLine[-1] == enterNumber):
                subLine.pop()
                enterNumber += 1
            # 1-3-2. 바로 입장할 수 없다면, 현재 대기열에서도 이동할 수 없고 임시 대기열에서도 이동이 불가능하므로 Sad를 출력한다.
            else :
                print("Sad")
                break
    # 2. 임시 대기열에만 사람이 있다면 이동이 가능한 지 확인한다.
    elif (len(subLine) != 0):
        # 2-1. 임시 대기열에서 바로 입장할 수 있다면 스택에서 삭제하고, enterNumber를 1 증가시킨다.
        if (subLine[-1] == enterNumber):
            subLine.pop()
            enterNumber += 1
        # 2-2. 바로 입장할 수 없다면, 현재 대기열에서도 이동할 수 없고 임시 대기열에서도 이동이 불가능하므로 Sad를 출력한다.
        else :
            print("Sad")
            break
    # 두 스택이 모두 비어있다면 성공적으로 이동이 완료된 것이므로 Nice를 출력한다.
    else :
        print("Nice")
        break