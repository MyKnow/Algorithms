import sys

input = sys.stdin.readline

# * Parameters
# - target: Int -> Number of router to want install
# - lst: list[Int] -> Coordinates of each houses (Sorted in ascending order)
#
# * Return
# - end: Maximum distance between two neighboring router
def binarySearch(target: int, lst: list[int]) -> int:
    # Minimum distance is 1
    start = 1
    
    # Maximum distance is distance between last and first
    end = lst[-1] - lst[0]

    while(start <= end):
        mid = (start+end) // 2

        # Position of last house where the router was installed
        lastPoint = lst[0]

        # Number of house where router is installed
        # initial: 1 (installed in lastPoint)
        count = 1

        for idx in range(1, len(lst)):
            crtPoint = lst[idx]

            # When distance between the previous house and 
            # the current house is same to "mid" or greater
            if crtPoint - lastPoint >= mid:
                lastPoint = crtPoint
                count += 1

        if target <= count:
            start = mid + 1
        else:
            end = mid - 1
            
    return end

N, C = map(int, input().split())

X = [int(input()) for _ in range(N)]
X.sort()

print(binarySearch(C, X))