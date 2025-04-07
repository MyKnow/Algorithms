// N: Int
// description: An integers that representing number of cities
// range: 2 ≤ N ≤ 100,000
if let inputOfN: String = readLine(), let N: Int = Int(inputOfN) {
    if let inputOfLengths: String = readLine(), let inputOfPrices: String = readLine() {
        // lengths: [Int] (immutable)
        // description: An array of integers representing the length of roads connecting each city
        // range: 1 ≤ length ≤ 1,000,000,000
        // length: N-1
        let lengths: [Int] = inputOfLengths.split(separator: " ").compactMap { Int($0) }

        // prices: [Int] (immutable)
        // description: An array of integers representing the refuelling cost for each city
        // range: 1 ≤ length ≤ 1,000,000,000
        // length: N
        let prices: [Int] = inputOfPrices.split(separator: " ").compactMap { Int($0) }

        // price: Int (mutable)
        // description: An integer to store minimum cost of refuelling
        // initial: First element of "prices"
        var price: Int = prices[0]

        // total: Int
        // description: An integer to store the total price of refuelling
        // initial: 0
        var total: Int = 0

        for idx in 0..<N-1 {
            // Update "total" as minimum cost multiplied by current road length
            total += price * lengths[idx]
        
            // Minimum cost of refuelling(called by price) update when the next cost(prices[idx+1]) is smaller
            if price > prices[idx+1] {
                price = prices[idx+1]
            }
        }
        
        // Print answer
        print(total)
    }
}