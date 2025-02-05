# [int] N: 입력 받을 회원 정보의 개수 (범위(정수): 1 ≤ N ≤ 100,000)
N = int(input())

# [list(tuple(int, int))] listOfPeople: 입력 받은 좌표를 저장하는 리스트 (길이: N)
listOfPeople = []

for index in range(N):
    # [tuple(int, string)] age, name: 입력 받은 나이와 이름을 저장하는 변수
    age, name = input().split()
    # 나이를 정수로 변환
    age = int(age)
    
    listOfPeople.append( (index, age, name) )

# 리스트를 나이 순, 나이가 같으면 인덱스 순으로 정렬한다.
listOfPeople.sort(key = lambda x: (x[1], x[0]))

# 출력
for _, age, name in listOfPeople:
    print(f"{age} {name}")