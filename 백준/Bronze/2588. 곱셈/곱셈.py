number1 = int(input())
number2 = int(input())

number3 = (number1 * (number2 % 10))
number4 = (number1 * (number2 // 10 % 10))
number5 = (number1 * (number2 // 100))

print(number3)
print(number4)
print(number5)
print(number1*number2)
