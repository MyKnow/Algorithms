import sys

input = sys.stdin.read
print = sys.stdout.write

data = input().split()

# N: int
# description: An integer representing count of numbers
# range: 1 ≤ N ≤ 1_000_000
N = int(data[0])

# M: int
# description: An integer that divides the sum of consecutive intervals so that the remainder becomes zero.
# range: 2 ≤ M ≤ 1,000
M = int(data[1])

# A: list
# description: A list of integers that stores the Nth number to obtain the number of intervals 
# whose remainder is zero when the sum of consecutive intervals is divided by M
# range: 0 ≤ A_i ≤ 10^9
# length: N
A = list(map(int, data[2:]))

# remainders: list
# description: A list of integers to store remainders of A's prefix sum divided by M
# length: M
remainders = [0] * M

# pSum: int
# description: An integer to store A's current prefix sum
# initial: 0
pSum = 0

# count: int
# description: An integer to store number of intervals 
# whose remainder is zero when the sum of consecutive intervals is divided by M
count = 0

for num in A:
    # Update the pSum to the previous pSum + current number of A
    pSum += num

    # Obtain remainder between pSum and M
    remainder = pSum % M

    # Increase the count when remainder is 0
    if remainder == 0:
        count += 1

    # Increase the remainders of current index
    remainders[remainder] += 1

# Update the count variable with the remaining number stored in "remainers".
# r * (r-1) // 2: number of consecutive intervals
count += sum(r * (r - 1) // 2 for r in remainders)  

# Print answer
print(f"{count}\n")