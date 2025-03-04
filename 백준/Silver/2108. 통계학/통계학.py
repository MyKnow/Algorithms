import sys

input = sys.stdin.readline

# [int] N: 수의 개수 (범위(자연수): 1 ≤ N ≤ 500,000)
N = int(input())

# [dict(int: int)] dic: 최빈값 계산을 위한 수: 개수 쌍 사전
dic = dict()

# [list(int)] lst: 중앙값 계산을 위한 리스트
lst = list()

# [int] sumOfNumbers: 총 합계를 저장하는 변수 (초기값: 0)
sumOfNumbers = 0

for _ in range(N):
    number = int(input())
    
    # 해당 수가 이미 사전에 있으면 개수를 증가시킨다.
    if (number in dic):
        dic[number] += 1
    # 없다면 사전에 추가한다.
    else:
        dic[number] = 0
    
    sumOfNumbers += number
    lst.append(number)
    
# 1. 산술평균 출력 (총 합계 나누기 개수의 결과에서 소수점 첫째 자리 반올림)
# 이 때 sumOfNumbers가 음수라면 절대값을 취한 뒤 음수로 재변환한다.
print(round(sumOfNumbers / N) if sumOfNumbers >= 0 else -round(abs(sumOfNumbers)/N))

# 2. 중앙값 출력 (리스트의 중간)
sortedList = sorted(lst)
print(sortedList[(len(lst)-1) // 2])

# 3. 최빈값 출력 (사전에서 빈도를 중심으로 오름차순 정렬하여, 가장 높은 값을 출력)
# 이 때 최빈값이 여러개 있는 경우, 최빈값 중 두번째로 작은 값을 출력함.
# 3-1. 사전의 값에서 최빈값 추출
mode = max(dic.values())
# 3-2. 사전을 순회하며 value가 mode인 키를 모두 리스트에 저장함
modeList = [key for key, value in dic.items() if value == mode]
# 3-3. modeList의 길이가 1이라면 그대로 출력, 아니라면 정렬하여 2번째로 작은 요소를 출력
print(modeList[0] if len(modeList) == 1 else sorted(modeList)[1])

# 4. 범위 출력
print(max(lst) - min(lst))