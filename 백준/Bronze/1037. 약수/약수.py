# [int] lenOfDivisor: 약수의 개수 (범위(자연수): 1 <= N <= 50)
N = int(input())

# [list(int)] listOfDivisor: 1과 N을 제외한 N의 약수를 오름차순 정렬한 리스트
# 범위(자연수): 2 <= divisor <= 1,000,000, 중복없음.
listOfDivisor = sorted(map(int, input().split()))

# 첫번째와 마지막 요소를 서로 곱하면 원래 수가 나온다.
print(listOfDivisor[0]*listOfDivisor[-1])