# [int] N : 숫자의 개수 (1 <= N <= 100)
N = int(input())

# [string] numbers : 공백 없이 연결된 숫자들의 문자열 (길이: N)
numbers = input()

# [int] sumOfNumbers : 각 숫자들의 총 합계
sumOfNumbers = 0

# numbers를 for문을 통해 하나씩 sumOfNumbers에 더한다.
for number in numbers :
    sumOfNumbers += int(number)

# sumOfNumbers을 출력한다
print(sumOfNumbers)