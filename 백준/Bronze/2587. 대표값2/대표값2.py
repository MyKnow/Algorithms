import sys

# [list(int)] sortedList: 입력된 숫자를 저장하고 정렬한 리스트 (길이: 1 <= N <= 1,000)
sortedList = sorted(list(map(int, (sys.stdin.read().split()))))

print(f"{sum(sortedList)//len(sortedList)}\n{sortedList[2]}")