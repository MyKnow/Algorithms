# [tuple(string, string)] A, B : 서로 같지 않고 0을 포함하지 않는, 두 개의 세 자리 수
A, B = input().split()

# [tuple(int, int)] reversedNumbers : 각 수의 문자열을 역으로 저장한 튜플 (길이 : 2)
reversedNumbers = map(lambda x: int(x[::-1]), (A, B))

# [int] bigger : 두 수 중에서 크기가 큰 수
bigger = max(reversedNumbers)

# 출력
print(bigger)