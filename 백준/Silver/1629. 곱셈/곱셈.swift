// pow: func(Int, Int, Int) -> Int
// description: A recursive function that calculates the results of formula "A * B % C" 
// by means of exponential law and remaining distribution law
func pow(_ a: Int, _ b: Int, _ c: Int) -> Int {
    // Return the result of "a mod c" when the exponent is 1
    if b == 1 {
        return a % c
    }
    // Return 1 when exponent is 0
    else if b == 0 {
        return 1
    }

    // half: Recursive call by "exponential law"
    let half: Int = pow(a, b / 2, c)

    // Return the result of the formula by "remaining distribution law"
    if b % 2 == 0 {
        return (half * half) % c
    }
    else {
        // Multiply square of "half" by more "a" when exponent is odd
        return ((half * half) % c * a % c) % c
    }
}

if let input: String = readLine() {
    let arrayOfInput: [Int] = input.split(separator: " ").compactMap { Int($0) }
    
    // A, B, C: Int
    // description: Integers used to calculate the formula "A*B%C" 
    let (A, B, C): (Int, Int, Int) = (arrayOfInput[0], arrayOfInput[1], arrayOfInput[2])


    // Call the function and print results
    print(pow(A, B, C))
}