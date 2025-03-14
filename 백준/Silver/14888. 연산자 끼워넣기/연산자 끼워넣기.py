# [int] N: Length of A (range(Integer): 2 ≤ N ≤ 11)
N = int(input())

# [list(int)] A: List of operand (length: N)
A = list(map(int, input().split()))

# [list(int)] O: Number of addition, subtraction, multiplication, and division (length: 4, sum: N-1)
O = list(map(int, input().split()))

# [int] maxDepth: Integer that defines maximum depth of solution function
maxDepth = sum(O)+1

# [int] maxValue, minValue
# : Integers that define limit range of maximum and minimum value of solution function
maxValue = -1_000_000_000
minValue = 1_000_000_000

# [def (depth: int, result: int)] solution
# : Function to Update maxValue and minValue of results through backtracking
def solution(depth: int, result: int):
    # Import maxValue and minValue as global variables.
    global maxDepth, maxValue, minValue
    
    # If "depth" reaches limit, both values are updated, and return
    if (depth == maxDepth):
        maxValue = max(maxValue, result)
        minValue = min(minValue, result)
        return
    
    # [int] nowOperand:
    # Integer to be used to calculating with result at now depth
    nowOperand = A[depth]
    
    # If "depth" is "0", Instantly call function with next depth for update "result".
    if (depth == 0):
        solution(1, A[depth])
    
    # Calculate with backtracking to obtain maxValue and minValue.
    for op, count in enumerate(O):
        # Calculate using only remaining operators
        if count > 0:
            # Reduce the count of current operator.
            O[op]-=1
            
            # Update "result" with backtracking.
            # Addition
            if (op == 0):
                result += nowOperand
                solution(depth+1, result)
                O[op]+=1
                result -= nowOperand
            # subtraction
            elif (op == 1):
                result -= nowOperand
                solution(depth+1, result)
                O[op]+=1
                result += nowOperand
            # multiplication
            elif (op == 2):
                result *= nowOperand
                solution(depth+1, result)
                O[op]+=1
                result //= nowOperand
            # division
            elif (op == 3):
                # Considering the constraints in Problem.
                if result < 0:
                    result = -(abs(result) // nowOperand)
                else:
                    result //= nowOperand
                solution(depth+1, result)
                O[op]+=1
                result *= nowOperand

# Update maxValue and minValue
solution(0, 0)
            
# print answers
print(maxValue)
print(minValue)