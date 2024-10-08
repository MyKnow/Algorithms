let number1: Int = Int(readLine() ?? "100") ?? 100
let number2: Int = Int(readLine() ?? "100") ?? 100

let number3: Int = number1 * (number2%10)
let number4: Int = number1 * (number2/10%10)
let number5: Int = number1 * (number2/100)

print(number3)
print(number4)
print(number5)
print(number1*number2)