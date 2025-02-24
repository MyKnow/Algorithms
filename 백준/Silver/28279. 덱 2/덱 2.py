from collections import deque
import sys

# [list(str)] commandList: 모든 명령어를 한 번에 저장한 리스트
commandList = sys.stdin.readlines()

# [int] N: 명령어의 수 (범위(자연수): 1 ≤ N ≤ 1,000,000)
N = int(commandList[0])

# [deque(str)] dq: int를 저장하는 deque
dq = deque()

# [list(str)] result: 각 명령어의 수행 결과를 저장하는 리스트(길이: <= N)
result = list()

for index in range(1, N+1):
    # [str] command: 현재 명령어
    command = commandList[index].strip()
    
    # 1, 2. append
    if (len(command) != 1):
        # [list(str)] splitedCommand: 분리된 명령어 (길이: 2)
        splitedCommand = command.split(" ")
        
        # 1. appendleft()
        if (splitedCommand[0] == "1"):
            dq.appendleft(splitedCommand[1])
        # 2. append()
        else:
            dq.append(splitedCommand[1])
    # 3. popleft()
    elif (command == "3"):
        result.append(dq.popleft() if len(dq) != 0 else "-1")
    # 4. pop()
    elif (command == "4"):
        result.append(dq.pop() if len(dq) != 0 else "-1")
    # 5. count
    elif (command == "5"):
        result.append(str(len(dq)))
    # 6. isEmpty
    elif (command == "6"):
        result.append("1" if len(dq) == 0 else "0")
    # 7. left
    elif (command == "7"):
        result.append(dq[0] if len(dq) != 0 else "-1")
    # 8. right
    elif (command == "8"):
        result.append(dq[-1] if len(dq) != 0 else "-1")
        
print("\n".join(result))