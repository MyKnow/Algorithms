// N: Int (Not used)
// description: An integer representing number of people withdrawing money
// range: 1 ≤ N ≤ 1,000
if let inputOfN: String = readLine(), 
    let _: Int = Int(inputOfN),
    let inputOfPi: String = readLine() {
        
    // Pi: [Int] (immutable)
    // description: An list of ascending sorted integers that
    // represents each person's withdrawal time.
    // range: 1 ≤ Pi ≤ 1,000
    // length: N
    let Pi: [Int] = inputOfPi.split(separator: " ").compactMap { Int($0) }.sorted(by: <)
        
    // latestTime: Int (mutable)
    // description: An integer to store the withdrawal time of the last person.
    // initial: 0
    var latestTime: Int = 0
    
    // totalTime: Int (mutable)
    // description: An integer to store sum of each latestTime
    // initial: 0
    var totalTime: Int = 0
    
    for t in Pi {
        latestTime += t
        totalTime += latestTime
    }
    
    print(totalTime)
}