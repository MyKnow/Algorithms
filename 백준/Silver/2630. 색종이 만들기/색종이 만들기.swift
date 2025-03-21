// [Int] N (immutable): An integer that represents the length of a square side
let N: Int = Int(readLine() ?? "2") ?? 2

// [Array<Array<Int>>] paper (mutable): 2-Dimensional array of integers to store blue and white colored papers
var paper = [[Int]]()

// Append to paper
for _ in 0..<N {
    let line: String = readLine() ?? "0 0"
    paper.append( line.split(separator: " ").compactMap{ Int($0) } )
}

// [Int] bCount, wCount (mutable): Integers to store number of each papers
var bCount: Int = 0
var wCount: Int = 0

// [func(Int, [[Int]]] solution
// : A Function that update bCount and wCount with greedy algorithm
//
// - Parameters
// [Int] n: An integer that represents the length of side of a now square
// [ Array<Array<Int>> ] m: 2-Dimensional array of integers that stores blue and white colored papers
func solution(
    _ n: Int, 
    _ m: [[Int]] 
) {
    // [Int] sumOfPaper (mutable): An integer that counts blue papers in m
    var sumOfPaper: Int = 0

    // Update sumOfPaper by sum of each line in "m"
    for row in m {
        sumOfPaper += row.reduce(0, +)
    }

    // If sumOfPaper is equal to n*n, then m is blue paper.
    if (sumOfPaper == n * n) {
        bCount += 1
    }
    // Otherwise, If sumOfPaper is 0, then m is white paper.
    else if (sumOfPaper == 0) {
        wCount += 1
    }
    // If neither, divide the paper into four and and do recursive call
    else {
        for p in divide(n, m) {
            solution(n/2, p)
        }
        
    }
}

// [ func(Int, [[Int]]) ] divide
// A Function that Divide original 2-D array into four 2-Dimensional array and return them as 3-Dimensional array
//
// - Parameters
// [int] n
// [Array<Array<Int>>] m
//
// - Return
// [ [[[Int]]] ]
func divide(_ n: Int, _ m: [[Int]] ) -> [[[Int]]] {
    var topLeft = [[Int]](repeating: [Int](repeating: 0, count: n/2), count: n/2)
    var topRight = [[Int]](repeating: [Int](repeating: 0, count: n/2), count: n/2)
    var botLeft = [[Int]](repeating: [Int](repeating: 0, count: n/2), count: n/2)
    var botRight = [[Int]](repeating: [Int](repeating: 0, count: n/2), count: n/2)

    for y in 0..<n {
        for x in 0..<n {
            if x < (n / 2) {
                if y < (n / 2) {
                    topLeft[y][x] = m[y][x]
                }
                else {
                    botLeft[y-(n / 2)][x] = m[y][x]
                }
            }
            else {
                if y < (n / 2) {
                    topRight[y][x-(n / 2)] = m[y][x]
                }
                else {
                    botRight[y-(n / 2)][x-(n / 2)] = m[y][x]
                }
            }
        }
    }
            
    return [ topLeft, topRight, botLeft, botRight ]
}

solution(N, paper)

print(wCount)
print(bCount)