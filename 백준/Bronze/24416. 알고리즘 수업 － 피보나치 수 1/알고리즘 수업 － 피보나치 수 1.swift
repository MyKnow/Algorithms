// [Int] n (immutable)
// : Integer that represents number for finding nth fibonacci
if let input: String = readLine(), let n: Int = Int(input) {
    // [Int] count (mutable)
    // : Integer to store the number of executions of dp function
    var dCount: Int = 0
    
    // [Array<Int>] fib (mutable)
    // : List of Integer to store the nth fibonacci
    var fib = [Int](repeating: 0, count: n+1)
    
    // First and Second numbers are 1
    fib[1] = 1
    fib[2] = 1
    
    // Repeat 3 through n to update fib
    for i in 3...n {
        // Updates dCount
        dCount += 1
        
        // Use pre-caculated values
        fib[i] = fib[i-1] + fib[i-2]
    }
    
    // Print a number of nth fibonacci and execution time of dp
    print("\(fib[n]) \(dCount)")
}