// [func (inout Int, inout Int, Int, Int, Int)] solution
// : Function to Update maxValue and minValue of results through backtracking
//
// - Parameter
// [Int] maxDepth
// [Int] depth
// [Int] result

func solution(
    _ maxDepth: Int,
    _ depth: Int, 
    _ result: Int
) {
    // If "depth" reaches limit, both values are updated, and return
    if (depth == maxDepth) {
        if let max = [maxValue, result].max() {
            maxValue = max
        }
        if let min = [minValue, result].min() {
            minValue = min
        }
        
        return
    }
    
    // [Int] nowOperand (immutable)
    // : Integer to be used to calculating with result at now depth
    let nowOperand: Int = A[depth]
    
    // If "depth" is "0", Instantly call function with next depth for update "result".
    if (depth == 0) {
        solution(maxDepth, 1, nowOperand)
    }
    
    // [Int] tmpResult (mutable)
    var tmpResult: Int = result
    
    // Calculate with backtracking to obtain maxValue and minValue.
    for (op, count) in O.enumerated() {
        // Calculate using only remaining operators
        if (count > 0) {
            // Reduce the count of current operator.
            O[op]-=1
            
            // Update "result" with backtracking.
            // Addition
            if (op == 0) {
                tmpResult += nowOperand
                solution(maxDepth, depth+1, tmpResult)
                O[op]+=1
                tmpResult -= nowOperand
            }
            // subtraction
            else if (op == 1) {
                tmpResult -= nowOperand
                solution(maxDepth, depth+1, tmpResult)
                O[op]+=1
                tmpResult += nowOperand
            }
            // multiplication
            else if (op == 2) {
                tmpResult *= nowOperand
                solution(maxDepth, depth+1, tmpResult)
                O[op]+=1
                tmpResult /= nowOperand
            }
            // division
            else if (op == 3) {
                // Considering the constraints in Problem.
                if tmpResult < 0 {
                    tmpResult = -(abs(tmpResult) / nowOperand)
                }
                else {
                    tmpResult /= nowOperand
                }
                solution(maxDepth, depth+1, tmpResult)
                O[op]+=1
                tmpResult *= nowOperand
            }
        }
    }
}
    
    
            


let input: String = readLine() ?? "2"

// [Int] N (immutable): Length of A (range(Integer): 2 ≤ N ≤ 11)
let N: Int = Int(input) ?? 2

// [Array<Int>] A (mutable): List of operand (length: N)
var A: [Int] = (readLine() ?? "1")
    .split(separator: " ")
    .compactMap { Int($0) }

// [Array<Int>] O (mutable)
// : Number of addition, subtraction, multiplication, and division (length: 4, sum: N-1)
var O: [Int] = (readLine() ?? "1")
    .split(separator: " ")
    .compactMap { Int($0) }

// [Int] maxDepth (immutable)
// : Integer that defines maximum depth of solution function
let maxDepth = O.reduce(0, +) + 1

// [Int] maxValue, minValue (mutable)
// : Integers that define limit range of maximum and minimum value of solution function
var maxValue: Int = -1_000_000_000
var minValue: Int = 1_000_000_000

// Update maxValue and minValue
solution(maxDepth, 0, 0)

// print answers
print(maxValue)
print(minValue)