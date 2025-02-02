# [int] n: 가장 아랫부분의 정사각형 개수 (범위: 1 <= n <= 10^9)
n = int(input())
    
# [int] lengthOfCoupleStair: 계단처럼 생긴 부분의 길이 * 2
# 마지막 사각형 밑변 전까지의 길이를 계산하는 데 쓰인다.
lengthOfStair = 3

# [int] sumOfLength: 총 길이 합
# n까지 3씩 더하며, 마지막 n층에서는 밑바닥 길이를 뜻하는 n을 추가로 더한다.
sumOfLength = (lengthOfStair * n) + n
        
# 합계를 출력한다.
print(sumOfLength)