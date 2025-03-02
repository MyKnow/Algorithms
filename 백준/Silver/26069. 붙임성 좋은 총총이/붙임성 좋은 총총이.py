# [int] N: 사람들이 만난 기록의 수 (범위(자연수): 1 <= N <= 1,000)
N = int(input())

# [set(str)] rainbow: 무지개 댄스를 추는 사람의 집합
rainbow = set()
# ChongChong은 처음부터 무지개 댄스를 춘다.
rainbow.add("ChongChong")

for _ in range(N):
    # [list(str)] log: 만난 두 사람을 저장한 리스트 (길이: 2)
    log = input().split()
    
    # 만약 log 속 사람 중에 한 명이라도 rainbow 집합에 포함되어 있다면
    # 두 사람을 모두 rainbow 집합에 추가함.
    for people in log:
        if people in rainbow:
            rainbow.update(log)
            break

# 무지개 댄스를 추는 사람의 수를 출력
print(len(rainbow))