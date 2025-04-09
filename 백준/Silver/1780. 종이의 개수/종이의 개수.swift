import Foundation

// nM1, n0, nP1: Int (mutable)
// description: An integer that stores the number of papers with different values
var nM1: Int = 0
var n0: Int = 0
var nP1: Int = 0

// paper: [[Int]] (mutable)
// description: Each value of points in given paper
// range: -1, 0, 1
// length: N*N
var paper = [[Int]]()

// recursion: func(Int, Int, Int)
// description: A recursive function that checks if all elements in a square 
// submatrix are the same, and if not, divides it into 9 zones and recursively processes each
// x: Int (start row index)
// y: Int (start column index)
// size: Int (length of square submatrix)
func recursion(_ x: Int, _ y: Int, _ size: Int) {
    // first: First value in current submatrix
    let first: Int = paper[x][y]

    // same: Bool (flag)
    // description: Flag to indicate if all values in the current submatrix are the same
    var same: Bool = true

    // Check if all values in submatrix are the same as first
    for i in x..<x + size {
        for j in y..<y + size {
            if paper[i][j] != first {
                same = false
                break
            }
        }
        if !same { break }
    }

    // If all values are the same, increment corresponding counter
    if same {
        if first == -1 {
            nM1 += 1
        } else if first == 0 {
            n0 += 1
        } else {
            nP1 += 1
        }
        return
    }

    // newSize: Int
    // description: Size of each divided zone (1/3 of current size)
    let newSize: Int = size / 3

    // Recursive call: divide into 9 zones
    for dx in 0..<3 {
        for dy in 0..<3 {
            // x + dx * newSize, y + dy * newSize: Starting point of subzone
            recursion(x + dx * newSize, y + dy * newSize, newSize)
        }
    }

    return
}

// N: Int
// description: size of given paper
// range: 1 ≤ N ≤ 3^7 (3^k)
if let inputOfN: String = readLine(), let N: Int = Int(inputOfN) {
    // Append each line to list "paper" 
    for _ in 0..<N {
        if let line: String = readLine() {
            paper.append( line.split(separator: " ").compactMap { Int($0) } )
        }
    }

    // Call function
    recursion(0, 0, N)

    // Print answer
    print(nM1)
    print(n0)
    print(nP1)
}