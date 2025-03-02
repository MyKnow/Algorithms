import sys

# Enter를 기준으로 전체 입력을 분할하여 리스트에 넣고, N을 제거함.
logForEachPeople = sys.stdin.read().split("ENTER")
logForEachPeople = logForEachPeople[1:]

# [int] count: 이모티콘이 사용된 횟수 (초기값: 0)
count = 0

# 각 ENTER마다 순회
for log in logForEachPeople:
    # log에서 사람마다 분할하여 집합에 넣고, 그 길이를 count에 더함.
    count += len(set(log.split()))
    
# 출력
print(count)