# [def(int)] dp
# : Function that updates number of execution: dCount
# and returns integer of n-th fibonacci
#
# - Parameters
# [int] n: Integer that represents number for finding nth fibonacci
#
# - Return
# [int] fib[n]: Integer of nth fibonacci
def dp(n: int):
    global dCount

    # [list] fib: List of "nth fibonacci" at each index
    fib = [0] * (n + 1)
    
    # First and Second numbers are 1
    fib[1] = fib[2] = 1
    
    # Repeat 3 through n to update fib
    for i in range(3, n+1):
        # Updates dCount
        dCount += 1
        # Use pre-caculated values
        fib[i] = fib[i-1] + fib[i-2]
    
    # Return fib[n] that number of nth fibonacci
    return fib[n]

# [int] n: Integer that represents number for finding nth fibonacci
n = int(input())

dCount = 0

# Number of recursive function executions, rCount is 
# same to nth fibonacci
rCount = dp(n)

print(f"{rCount} {dCount}")