import Foundation

// pow: func(Int, Int, Int) -> Int
// description: A function that returns result of pow operator
// with modular operator using fast exponentiation
func pow(_ num: Int, _ exp: Int, _ mod: Int) -> Int {
    var result: Int = 1
    var num: Int = num % mod
    var exp: Int = exp

    while exp > 0 {
        if exp % 2 == 1 {
            result = (result * num) % mod
        }
        num = (num * num) % mod
        exp /= 2
    }

    return result
}

if let input: String = readLine() {
    let arrayOfInput: [Int] = input
        .split(separator: " ")
        .compactMap { Int($0) }
    
    // N: Int (immutable)
    // description: Total number of items
    let (N, K): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])
    
    // MOD: Int (immutable)
    // description: A prime number for modulo operations
    let MOD: Int = 1_000_000_007

    // Special case: C(N, 0) = 1
    if K == 0 {
        print(1)
        exit(0)
    }

    // numerator: Int
    // description: Stores product of N * (N-1) * ... * (N-K+1) % MOD
    var numerator: Int = 1
    for n in (N - K + 1)...N {
        numerator *= n
        numerator %= MOD
    }

    // denominator: Int
    // description: Stores K! % MOD
    var denominator: Int = 1
    for k in 1...K {
        denominator *= k
        denominator %= MOD
    }

    // denominatorInv: Int
    // description: Stores modular inverse of denominator using Fermat's Little Theorem
    let denominatorInv: Int = pow(denominator, MOD - 2, MOD)

    // result: Int
    // description: The final combination result (C(N, K) % MOD)
    let result: Int = numerator * denominatorInv % MOD
    print(result)
}