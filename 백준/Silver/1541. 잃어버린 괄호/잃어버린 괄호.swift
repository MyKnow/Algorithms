if let inputOfExp: String = readLine() {
    // exp: [String] (immutable)
    // description: An array of strings that store each sub expression that splited by "-"
    let exp: [String] = inputOfExp.split(separator: "-").map { String($0) }

    // splitByPlus: [Int] (immutable)
    // description: An array of integers that store results of 
    // each sub expression that splited by "+" from exp
    let splitByPlus: [Int] = exp.map { $0.split(separator: "+").compactMap { Int($0) }.reduce(0, +) }
    
    // Print result of subtracting between each sub expression
    print(splitByPlus[0] - (splitByPlus[1...].reduce(0, +)))
}