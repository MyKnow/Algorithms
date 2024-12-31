# [function] getResultWithoutMethod
#
# Notes
# - min, max 메서드 없이 int list의 최소/최대값을 산출하는 함수
#
# Parameters
# - [list] arr : 값을 산출하고자 하는 list
#
# Returns
# - [tuple] (minOfArr, maxOfArr) : 최소값, 최대값 튜플
# 
def getResultWithoutMethod(arr):
    # [int] minOfArr : 최소값을 저장하는 변수 (입력 제한의 상한 기준)
    # [int] maxOfArr : 최대값을 저장하는 변수 (입력 제한의 하한 기준)
    minOfArr = 1000000
    maxOfArr = -1000000

    # list를 탐색하며 최솟값과 최댓값을 수정함
    for number in arr:
        if (number < minOfArr) :
            minOfArr = number
        if (number > maxOfArr) :
            maxOfArr = number
            
    return minOfArr, maxOfArr

# [int] N : 정수의 개수 (1 <= N <= 1,000,000)
N = int(input())

# [list] arr : 입력 받은 정수를 저장한 리스트
arr = map(int, input().split())

minOfArr, maxOfArr = getResultWithoutMethod(arr)
 
# 각 값을 출력
print(minOfArr, maxOfArr)