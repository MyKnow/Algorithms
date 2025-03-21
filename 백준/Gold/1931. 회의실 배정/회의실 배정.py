import sys

input = sys.stdin.readline

# [int] N: An Integer that represents number of meeting(range: 1 ≤ N ≤ 100,000)
N = int(input())

# [int] lastEnd: An Integer that stores last meeting time
lastEnd = 0

# [int] count: An Integer that stores the number of meetings
count = 0

# [list(tuple)] listOfTuple: List of tuple of integers that 
# stores start and end time of each meetings
listOfTuple = list()

for _ in range(N):
    # [int] start, end: Start and end times of the now meeting
    start, end = map(int, input().split())
    listOfTuple.append( (start, end) )

# Sort by end time of meetings
listOfTuple.sort(key= lambda x: (x[1], x[0]))

for start, end in listOfTuple:
    # Update count and lastEnd when start is later than or equal to lastEnd
    if (start >= lastEnd):
        count += 1
        lastEnd = end

print(count)