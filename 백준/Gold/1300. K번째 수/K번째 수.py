N = int(input())
K = int(input())

# Index starts at 1
start = 1

# Kth number isn't greater than K
end = K

while (start <= end):
    mid = (start+end) // 2

    # Count of numbers less than "mid" in list B
    total = 0

    for i in range(1, N+1):
        # mid // i : Column index smaller than "mid" value in row i
        total += min(mid // i, N)

    # When "mid" smaller than B[K]
    if total < K:
        start = mid + 1
    else:
        end = mid - 1

print(end+1)