import sys
import heapq

input = sys.stdin.readline
write = sys.stdout.write

T = int(input())

for _ in range(T):
    # Length of sequence
    M = int(input())
    print((M // 2) + 1)

    # MaxHeap
    left = []
    # MinHeap
    right = []

    count = 0
    result = []

    nums = []
    while len(nums) < M:
        nums += list(map(int, input().split()))

    for i in range(M):
        num = nums[i]

        if not left or num <= -left[0]:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        # Balance heaps
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

        # Collect middle values (only when index is even)
        if i % 2 == 0:
            write(str(-left[0]))
            count += 1
            if count % 10 == 0:
                write("\n")
            else:
                write(" ")
    write("\n")