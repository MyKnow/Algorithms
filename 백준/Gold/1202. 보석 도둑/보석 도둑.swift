import Foundation

// (Weight, Price) tuple of jewels
struct Jewel: Comparable {
    let weight: Int
    let price: Int
    
    static func < (lhs: Jewel, rhs: Jewel) -> Bool {
        return lhs.price < rhs.price
    }
}

// Max heap
struct MaxHeap<T: Comparable> {
    private var heap = [T]()
    var isEmpty: Bool { heap.isEmpty }
    
    mutating func push(_ value: T) {
        heap.append(value)
        var i = heap.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if heap[p] >= heap[i] { break }
            heap.swapAt(p, i)
            i = p
        }
    }
    
    mutating func pop() -> T? {
        if heap.isEmpty { return nil }
        if heap.count == 1 { return heap.removeFirst() }
        let top = heap[0]
        heap[0] = heap.removeLast()
        var i = 0
        while true {
            let l = i * 2 + 1
            let r = l + 1
            var t = i
            if l < heap.count && heap[l] > heap[t] { t = l }
            if r < heap.count && heap[r] > heap[t] { t = r }
            if t == i { break }
            heap.swapAt(i, t)
            i = t
        }
        return top
    }
}

guard let inputOfNK = readLine() else { exit(0) }
let arrayOfNK = inputOfNK.split(separator: " ").compactMap { Int($0) }
// N: Number of jewels
let N = arrayOfNK[0]
// K: Number of bags
let K = arrayOfNK[1]

var jewels = [Jewel]()
for _ in 0..<N {
    guard let line = readLine() else { exit(0) }
    let parts = line.split(separator: " ").compactMap { Int($0) }
    jewels.append(Jewel(weight: parts[0], price: parts[1]))
}
jewels.sort { $0.weight < $1.weight }

// Array of bag weight limits
var bags = [Int]()
for _ in 0..<K {
    guard let line = readLine(), let c = Int(line) else { exit(0) }
    bags.append(c)
}
bags.sort(by: <)

// Max heap
var maxHeap = MaxHeap<Jewel>()

// Total price of jewels
var total = 0

// Current index of jewels
var jewelIdx = 0
for capacity in bags {
    // Heappush jewels to maxHeap which can insertable to bag
    while jewelIdx < N && jewels[jewelIdx].weight <= capacity {
        maxHeap.push(jewels[jewelIdx])
        jewelIdx += 1
    }

    // Choose the largest price and add it to "total"
    if let pop = maxHeap.pop() {
        total += pop.price
    }
}

// Print answer
print(total)