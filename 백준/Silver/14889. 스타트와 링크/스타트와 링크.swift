// [func(Int, inout [Int])] updateArrayOfTeams
// Function that updates a global array called "arrayOfTeams"
//
// - Parameters
// [Int] depth: Integer that used for backtracking
// [inout Array<Int>]] stack: Integer list that represents possible combinations of start team.
func updateArrayOfTeams(_ depth: Int, _ stack: inout [Int]) {
    if (depth == N / 2) {
        let t1: Set<Int> = Set(stack)
        // [Set(int)] t2 (immutable)
        // : Obtain set of link team by difference between 
        // set of all members and t1
        let t2: Set<Int> = Set(0..<N).subtracting(t1)

        // Group to start and link teams into a 
        // list, and append them to arrayOfTeams.
        arrayOfTeams.append( [t1, t2] )

        return
    }

    // For optimization
    if let first = stack.first, first != 0 {
        return
    }

    // [Int] start (immutable)
    // : Define start indexbased on stack length for non-decreasing sort 
    var start: Int = 0
    if let top: Int = stack.last {
        start = top + 1
    }

    // Get number of Member
    for member in start..<N {
        // Append member into stack
        stack.append(member)
        
        // Try appending next member
        updateArrayOfTeams(depth+1, &stack)

        // Backtracking
        stack.removeLast()
    }
}

// [func(Set<Int>)) -> Array<(Int, Int)>] getCombinations
// Function that returns array of possible combinations of source to non-decreasing sort
//
// - Parameter:
// [Set<Int>] team: Set of int to create combinations
//
// - Return:
// [Array<(Int, Int)>]: List of combinations
func getCombinations(_ team: Set<Int>) -> Array<(Int, Int)> {
    // Append (i, j) tuple into tempArray by non-decreasing sort
    var tempArray = [(Int, Int)]()
    for i in team {
        for j in team {
            if i < j {
                tempArray.append( (i, j) )
            }
        }
    }

    return tempArray
}

// [Int] N (immutable) 
// : Integer representing number of people (range(even): 4 ≤ N ≤ 20)
let N: Int = Int(readLine() ?? "4") ?? 4

// [Array<Array<Int>>] S
// : 2-Dimensional array that represents status of each combinations
var S: [[Int]] = []
for _ in 0..<N {
    S.append((readLine() ?? "0").split(separator: " ").compactMap { Int($0) })
}

// [Array<Array<Set<Int>>>] arrayOfTeams
// : 2-Dimensional array that including set of possible team distribution
var arrayOfTeams = [[Set<Int>]]()

// Update arrayOfTeams
var tmpArray = [Int]()
updateArrayOfTeams(0, &tmpArray)

// Update minValue
// Get member array of both team
var minValue: Int = (100-1) * 20
for team in arrayOfTeams {
    // [Array<Int>] result
    // : Array of integer for calculate minValue
    var result: [Int] = [0, 0]
    
    // Get index and each team
    for (idx, t) in team.enumerated() {
        // Get possible combinations for each team and update the result.
        for (i, j) in getCombinations(t) {
            result[idx] += (S[i][j] + S[j][i])
        }
    }
    // Calculate diff between result[0] and result[1]
    let diff: Int = abs(result[0] - result[1])

    // Update minValue
    if (minValue > diff) {
        minValue = diff
    }
}

print(minValue)