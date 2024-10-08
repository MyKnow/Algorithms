let year: Int = Int(readLine() ?? "1") ?? 1

let condOfMul4 = (year % 4 == 0)
let condOfNotMul100orMul400 = (year % 100 != 0) || (year % 400 == 0)

if (condOfMul4 && condOfNotMul100orMul400) {
    print(1)
} else {
    print(0)
}