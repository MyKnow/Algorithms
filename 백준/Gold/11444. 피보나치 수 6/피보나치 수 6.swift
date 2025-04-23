// memo: Dictionary<Int, Int> (mutable)
// description: A dictionary of {Int, Int} pairs
// to optimize Fibonacci numbers finding
var memo: Dictionary<Int, Int> = [
    0:0,
    1:1,
]
// div: Int (immutable)
// description: An integer to perform fibonacci number
// and a division operation.
let div: Int = 1_000_000_007

// fibonacci: func(Int) -> Int
// description: A function to find nth fibonacci number
// with "d'Ocagne's identity"
//
// d'Ocagne's identity:
// original: F_m+n = F_m-1 * F_n + F_m * F_n+1
// when idx is even number: (m=n) -> F_2n = F_n(F_n+2F_{n-1})
// when idx is odd number: (m=n+1) -> F_2n+1 = = F_n^2+F_{n+1}^2
//
// Parameter
// idx: Int -> That represents index of fibonacci number
//
// Return
// memo[idx]: Int -> fibonacci number at idx
func fibonacci(_ idx: Int) -> Int {
    if let value: Int = memo[idx] {
        return value
    } else {
        // Update memo[idx] with d'Ocagne's identity
        let fn: Int = fibonacci(idx/2)
        
        var result: Int = 0
        
        if idx % 2 == 0 {
            let fnM1: Int = fibonacci(idx/2 - 1)
            result = ( fn * (fn + 2 * fnM1) ) % div
        }
        else {
            let fnP1: Int = fibonacci(idx/2 + 1)
            let left: Int = (fn*fn) % div
            let right: Int = (fnP1*fnP1) % div
            result = (left + right) % div
        }
        memo[idx] = result
        return result
    }
}

// n: Int (immutable)
// description: An integer that represents the 
// index to find the Fibonacci numbers
if let input: String = readLine(), let n: Int = Int(input) {
    // Print result
    print(fibonacci(n))
}