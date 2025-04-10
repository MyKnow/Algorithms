import sys
	
input = sys.stdin.readline

# pow: def(int, int, int) -> int
# description: A recursive function that calculates the results of formula "A * B % C" 
# by means of exponential law and remaining distribution law
def pow(a: int, b: int, c: int) -> int:
    # Return the result of "a mod c" when the exponent is 1
    if b == 1:
        return a % c

    # Recursive call by "exponential law"
    half = pow(a, b // 2, c)

    # Return the result of the formula by "remaining distribution law"
    if b % 2 == 0:
        return (half * half) % c
    else:
        # Multiply square of "half" by more "a" when exponent is odd
        return (half * half * a) % c

# A, B, C: int
# description: Integers used to calculate the formula "A*B%C" 
A, B, C = map(int, input().split())

# Call the function and print results
print(pow(A, B, C))