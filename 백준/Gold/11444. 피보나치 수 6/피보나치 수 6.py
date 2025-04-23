# n: int
# description: An integer that represents the 
# index to find the Fibonacci numbers
n = int(input())

# memo: dict(int:int)
# description: A dictionary of {int:int} pairs
# to optimize Fibonacci numbers finding
# initial: { 0:0, 1:1 }
memo = { 0:0, 1:1 }

# div: int
# description: An integer to perform fibonacci number
# and a division operation.
div = 1_000_000_007

# fibonacci: def(int) -> int
# description: A function to find nth fibonacci number
# with "d'Ocagne's identity"
#
# d'Ocagne's identity:
# original: F_m+n = F_m-1 * F_n + F_m * F_n+1
# when idx is even number: (m=n) -> F_2n = F_n(F_n+2F_{n-1})
# when idx is odd number: (m=n+1) -> F_2n+1 = = F_n^2+F_{n+1}^2
#
# Parameter
# idx: int -> That represents index of fibonacci number
#
# Return
# memo[idx]: int -> fibonacci number at idx
def fibonacci(idx: int) -> int :
    # Update memo[idx] with d'Ocagne's identity
    if not (idx in memo):
        fn = fibonacci(idx//2)
        if idx % 2 == 0:
            fnM1 = fibonacci(idx//2 - 1)
            memo[idx] = (fn * (fn + 2 * fnM1) ) % div
        else:
            fnP1 = fibonacci(idx//2 + 1)
            memo[idx] = (fn**2+fnP1**2) % div

    # Return fibonacci number at idx
    return memo[idx]

# Print result
print(fibonacci(n))