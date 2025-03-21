// [Int] N (immutable): An Integer that represents length of Ai (range: 1 ≤ N ≤ 10)
// [int] K (mutable): An Integer that represents the amount of money to be made (range: 1 ≤ K ≤ 100,000,000)
let input: [Int] = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let N: Int = input[0]
var K: Int = input[1]

// [Array<Int>] Ai (mutable): Array of Integers that store amount of each coin
var Ai = [Int]()

// Update Ai until coin is smaller than K
while let line: String = readLine(), let coin: Int = Int(line) {
    if (coin > K) {
        break
    }
    Ai.append( coin )
}

// Reverse Ai
Ai.sort(by: >)

// [Int] count (mutable): number of coins
var count: Int = 0
for coin in Ai {
    // Exit when K is 0
    if (K == 0) {
        break
    }
    // Update count
    count += (K / coin)
    
    // Update K
    K %= coin
}

print(count)