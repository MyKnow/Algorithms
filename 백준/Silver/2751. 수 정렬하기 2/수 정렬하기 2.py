import sys

# [list(int)] listOfNumbers: 입력된 N개의 수를 저장하는 리스트 (길이: N)
listOfNumbers = list(map(int, sys.stdin.read().split()))

# 첫번째 줄은 N을 입력 받는 곳이므로 삭제한다.
listOfNumbers = list(map(int, listOfNumbers[1:]))

# listOfNumbers를 정렬한다.
listOfNumbers.sort()

# listOfNumbers를 출력한다.
sys.stdout.write("\n".join(map(str, listOfNumbers)))