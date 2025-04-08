// isSingleColor: func([[Int]]) -> Bool
// description: A function that returns Boolean based on wheter the colors 
// in a given 2-Dimensional array are all the same color
func isSingleColor(_ v: [[Int]]) -> Bool {
    // firstColor: First color of  "v"
    let firstColor: Int = v[0][0]

    // Traveling the  v, return false if val is different color from the "firstColor"
    for row in v {
        for val in row {
            if val != firstColor {
                return false
            }
        }
    }

    // Return true when iteration completes search to the end.
    return true
}

// recursion: func([[Int]]) -> String
// description: A recursive function that converts a given 2-Dimensional 
// array into a quad tree and returns it as a string
func recursion(_ v: [[Int]]) -> String {
    // n: Number of rows in  v
    let n: Int = v.count

    // Return first color when no longer divisible or is a single color
    if (n == 1 || isSingleColor(v) == true) {
        return String(v[0][0])
    }

    // half: An integer representing index of half in  v
    let half: Int = n/2

    // top, bot: 2-Dimensional array of integers that stores array v divided
    // between top and bottom based on the "half" index
    let top: [[Int]] = Array(v[..<half])
    let bot: [[Int]] = Array(v[half...])

    // topLeft, ..., botRight: Lists that split list v into four based on half
    var topLeft = [[Int]]()
    var topRight = [[Int]]()
    var botLeft = [[Int]]()
    var botRight = [[Int]]()

    // Append to each list
    for i in 0..<half {
        topLeft.append(Array(top[i][0..<half]))
        topRight.append(Array(top[i][half..<n]))
        botLeft.append(Array(bot[i][0..<half]))
        botRight.append(Array(bot[i][half..<n]))
    }
        
    // Recurvise call divided into top-left, top-right, bottom-left, bottom-right zones
    // and add up the results. 
    return "(" +
        recursion(topLeft) +
        recursion(topRight) +
        recursion(botLeft) +
        recursion(botRight) +
    ")"
}

// N: Int (Not used)
// description: size of given video
// range: 1 ≤ N ≤ 64
if let inputOfN: String = readLine(), let _: Int = Int(inputOfN) {
    // video: [[Int]] (mutable)
    // description: Each color of points in given video
    // range: 0, 1
    // length: N*N
    var video = [[Int]]()

    // Append each line to list "video" 
    while let line: String = readLine() {
        video.append( line.compactMap { Int(String($0)) } )
    }
    
    // Print answer
    print(recursion(video))
}