import sys

input = sys.stdin.readline

# [def(int) -> list(int)] getPrimeNumberList: 2부터 target까지의 범위에 해당하는 소수 리스트를 반환하는 함수
def getPrimeNumberList(target):
    # [int] sqrtTarget: target의 제곱근
    sqrtTarget = int(target ** 0.5)
    
    # [list(bool)] listOfPrimeNumber: 인덱스가 소수일 때 값이 true인 리스트 (길이: target+1)
    listOfPrimeNumber = [True for _ in range(target+1)]
    
    # 0과 1은 소수가 아니므로 False로 변경한다.
    listOfPrimeNumber[0] = False
    listOfPrimeNumber[1] = False
    
    # 2부터 sqrtTarget+1까지 순회하며 listOfPrimeNumber를 업데이트한다.
    for index in range(2, sqrtTarget+1):
        # 만약 listOfPrimeNumber[index]가 True라면 index는 소수이다.
        # 따라서, index의 배수들은 소수가 아니다.
        if (listOfPrimeNumber[index]):
            # index의 배수를 모두 False로 변경한다.
            # 최적화를 위해 index*index부터 시작한다.
            # Target을 포함해서 수정해야 하므로 target+1까지 반복한다.
            # index의 배수를 업데이트 하므로 index 간격으로 반복한다.
            for mul in range(index*index, target+1, index):
                listOfPrimeNumber[mul] = False
                
    # 수정이 종료되면 value가 True인 index만을 추출하여 리스트로 만들고 반환한다.
    return [index for index, value in enumerate(listOfPrimeNumber) if value]

# [int] T: 테스트 케이스의 개수 (범위(자연수): 1 ≤ T ≤ 100)
T = int(input())

# [list(int)] listOfN: 각 테스트 케이스의 N을 저장한 리스트 (길이: T)
listOfN = []

for _ in range(T):
    # 골드바흐 파티션의 개수를 구할 짝수 (범위(자연수): 2 < N ≤ 1,000,000)
    listOfN.append(int(input()))
    
# [list(int)] listOfPN: 2부터 listOfN의 max값까지의 범위에 해당하는 소수 리스트
listOfPN = getPrimeNumberList(max(listOfN))

# [set(int)] setOfPN: listOfPN의 집합
setOfPN = set(listOfPN)

# [list(int)] listOfCounts: 각 테스트케이스 N에 대해서 발견한 골드바흐 파티션의 개수를 저장하는 리스트
listOfCounts = []

# listOfN을 순회하며 listOfCounts를 업데이트 한다.
for n in listOfN:
    count = 0
    for pn in listOfPN:
        # 소수가 목표 짝수의 절반보다 커지면 종료한다.
        if ((n//2) < pn):
            break
            
        # 현재 목표 짝수 n과 소수 pn에 대해서, n-pn이 setOfPN 안에 존재한다면 count를 증가시킨다.
        if (n-pn in setOfPN):
            count += 1
    
    # listOfCounts에 현재 count를 추가한다.
    listOfCounts.append(count)
    
# listOfCounts를 형식에 맞게 출력한다.
print("\n".join(map(str, listOfCounts)))