import sys
	
input = sys.stdin.readline
print = sys.stdout.write

exp = input() + " "

if ("-" not in exp):
    operands = map(int, exp.split("+"))
    print(f"{sum(operands)}\n")
elif ("+" not in exp):
    operands = list(map(int, exp.split("-")))
    print(f"{operands[0] - sum(operands[1:])}\n")
else:
    opStack = []
    lastOperator = ""
    op = ""
    
    for s in exp:
        if s.isnumeric():
            op += s
        else:
            if op:
                opInt = int(op)
                if lastOperator in ["+", " "]:
                    if opStack:
                        opStack[-1] += opInt
                    else:
                        opStack.append(opInt)
                else:
                    opStack.append(opInt)
                op = ""
            lastOperator = s
            
    print(f"{opStack[0] - sum(opStack[1:])}\n")