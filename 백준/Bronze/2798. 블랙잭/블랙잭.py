# [int] N: 카드의 개수 (범위: 3 <= N <= 100)
# [int] M: 딜러가 외치는 숫자 (범위: 10 <= M <= 300,000)
N, M = map(int, input().split())

# [list(int)] listOfCards: 카드들을 저장하는 리스트 (길이: N, 범위(자연수): < 100,000)
listOfCards = list(map(int, input().split()))

# listOfCards에 들어있는 카드 중 3개를 골라서 M에 최대한 근접하게 만들고, 그 합을 출력해야 한다.
# 시간 제한이 넉넉하므로, 삼중 중첩 반복문을 만들어서 모든 경우의 수를 계산하여 리스트에 저장하고, M에 근접한 값을 출력한다.

# [list(int)] listOfSums: 카드 3개의 합을 저장하는 리스트 (길이: 3)
listOfSums = []

for first in listOfCards:
    for second in listOfCards:
        for third in listOfCards:
            # 동일한 카드가 아닌 경우에만 리스트에 더한다.
            if (first != second and second != third and first != third):
                listOfSums.append(first+second+third)

# [int] index: 현재 리스트의 인덱스
index = 0

# 합계 리스트를 내림차순 정렬하고, M보다 작거나 같은 수를 찾을 때까지 index를 더한다.
listOfSums.sort(reverse = True)
while(listOfSums[index] > M):
    index+=1
    
    
# 해당 index-1에 있는 요소를 출력한다.
print(listOfSums[index])