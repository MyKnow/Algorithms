import Foundation

// MARK: - Constants

/// div: Int
/// description: An integer that performs each element and the
/// rest of the operation in the matrix multiplication operation
/// initial: 1,000
let div: Int = 1_000

// MARK: - Input

guard let inputOfNB: String = readLine() else {
    exit(-1)
}
let arrayOfNB: [Int] = inputOfNB.split(separator: " ").compactMap { Int($0) }

/// N: Int
/// description: An integer that represents size of matrix
/// range: 2 ≤ N ≤ 5
///
/// B: Int
/// description: An integer that represents number
/// of times the matrix will be squared
/// range: 1 ≤ B ≤ 100,000,000,000
let N: Int = arrayOfNB[0]
let B: Int64 = Int64(arrayOfNB[1])

/// A: [[Int]] (immutable)
/// description: 2-Dimensional list of integers that stores matrix
/// used for matrix squared operations
/// length: N * N
var A = [[Int]]()
for _ in 0..<N {
    guard let inputOfRow: String = readLine() else {
        exit(-2)
    }
    
    let row: [Int] = inputOfRow.split(separator: " ").compactMap { Int($0) }
    A.append(row)
}

/// memo: [Int64: [[Int]]]
/// description: A dictionary to store each
/// result of matrix power by exponent
/// key -> exponent: Int64
/// value -> matrix: [[Int]]
/// initial: 1: A
var memo: [Int64: [[Int]]] = [1: A]

// MARK: - Matrix Multiplication

/// matrixProduct: func(_ a:[[Int]], _ b: [[Int]]) -> [[Int]]
/// description: A function that returns the result of multiplying the matrix
/// a and b using the remaining operations
func matrixProduct(
    _ a: [[Int]], 
    _ b: [[Int]]
) -> [[Int]] {
    var result = [[Int]](
        repeating: [Int](
            repeating: 0, 
            count: N
        ), 
        count: N
    )
    
    for i in 0..<N {
        for j in 0..<N {
            var sum = 0
            for k in 0..<N {
                sum += (a[i][k] % div) * (b[k][j] % div)
            }
            result[i][j] = sum % div
        }
    }
    
    return result
}

// MARK: - Matrix Power (Recursive)

/// solution(_ exp: Int64) -> [[Int]]
/// description: A function that returns a matrix squared by given exponent
func solution(_ exp: Int64) -> [[Int]] {
    // Using memoization
    if let cached = memo[exp] {
        return cached
    }
    
    // result: A result of matrix squared by exponent//2
    let half = solution(exp / 2)
    var res = matrixProduct(half, half)
    
    // Exponential law
    if exp % 2 == 1 {
        res = matrixProduct(res, A)
    }
    
    memo[exp] = res
    return res
}

// MARK: - Output

/// Print answer
let answer = solution(B)
for row in answer {
    print(row.map { String($0 % div) }.joined(separator: " "))
}