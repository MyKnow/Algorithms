import sys

input = sys.stdin.readline

# [int] N: 채팅방의 기록 수 (범위(자연수): 1 <= N <= 100,000)
N = int(input())

# [set(str)] person: 각 ENTER 이후로 채팅을 친 유저의 집합
# 문자열 길이: 1 <= len <= 20
person = set()

# [int] count: 이모티콘이 사용된 횟수 (초기값: 0)
count = 0

for _ in range(N):
    # [str] log: 채팅방 로그
    log = input().strip()
    
    # 새로운 사람이 입장했다면 person을 초기화함.
    if (log == "ENTER"):
        person = set()
    # 그 외의 경우 채팅을 입력한 유저의 닉네임임.
    else:
        # 집합에 없는 닉네임인 경우, 집합에 추가하고 count를 증가시킴.
        if (log not in person):
            person.add(log)
            count+=1

# 한 번에 출력
print(count)