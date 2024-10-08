year = int(input())

condOf4x = year % 4 == 0
condOfNot100xOr400x = (year % 100 != 0) or (year % 400 == 0)
if (condOf4x and condOfNot100xOr400x) :
    print(1)
else :
    print(0)