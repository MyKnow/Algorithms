# [int] n: 회사 로그에 기록된 출입 기록의 수 (범위(자연수): 2 <= n <= 1,000,000)
n = int(input())

# [set(str)] setOfNames: 회사에 있는 모든 사람을 저장하는 집합 (크기: <= n)
setOfNames = set()

# N회 반복
for _ in range(n):
    # [str] name, act: 각 로그에 적힌 사람의 이름과 출입 여부
    name, act = input().split()
    
    # 출입로그 기록에 오류가 없다고 가정.
    # 로그에 enter라고 써 있으면 집합에 이름을 추가함.
    if (act == "enter"):
        setOfNames.add(name)
    # 로그에 leave라고 써 있으면 집합에서 이름을 찾아 제거함.
    else :
        setOfNames.remove(name)

# 완성된 로그를 리스트로 변환하고, 내림차순 정렬하여 출력
for name in sorted(list(setOfNames), reverse=True):
    print(name)