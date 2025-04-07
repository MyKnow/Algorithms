import sys
	
input = sys.stdin.readline
print = sys.stdout.write

# exp: list(str)
# description: A list of strings that store each sub expression that splited by "-"
exp = input().split("-")

# splitByPlus: list(list(str))
# description: 2-Dimensional list of strings that store results of 
# each sub expression that splited by "+" from exp
splitByPlus = list(map(sum, map(lambda x: map(int, x.split("+")), exp)))

# Print result of subtracting between each sub expression
print(f"{splitByPlus[0] - sum(splitByPlus[1:])}\n")