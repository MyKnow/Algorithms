struct MinHeap {
    private var heap = [Int]()
    
    // Check if the heap is empty
    public var isEmpty: Bool { heap.isEmpty }

    // Min-heap: returns true if parent is less than child
    @inline(__always)
    private func areSorted(_ parent: Int, _ child: Int) -> Bool { 
        heap[parent] < heap[child] 
    }

    // Min-heap push
    mutating func push(_ value: Int) {
        heap.append(value)

        var child: Int = heap.count - 1
        while child > 0 {
            // Index of the parent node
            let parent: Int = (child - 1) / 2

            // If sorted, stop
            if areSorted(parent, child) { break }

            // Swap parent and child
            heap.swapAt(parent, child)

            // Move up to parent
            child = parent
        }
    }

    // Min-heap pop
    mutating func pop() -> Int {
        // Return 0 if heap is empty
        if isEmpty {
            return 0
        } 
        // Return and remove the only element
        else if heap.count == 1 {
            return heap.removeFirst()
        }

        // Store the top value (minimum)
        let top: Int = heap[0]

        // Replace root with the last element
        heap[0] = heap.removeLast()

        var parent: Int = 0
        while true {
            var target: Int = parent
            let left: Int = parent * 2 + 1
            let right: Int = left + 1

            // Choose the smaller child
            if (left < heap.count) && !areSorted(target, left) { target = left }
            if (right < heap.count) && !areSorted(target, right) { target = right }

            // If already sorted, stop
            if parent == target { break }

            // Swap parent and target child
            heap.swapAt(parent, target)

            // Move down to target
            parent = target
        }

        return top
    }
}

let _ = readLine()

var pq = MinHeap()
var result = [Int]()

// Handle input
while let line: String = readLine(), let X: Int = Int(line) {
    if X == 0 {
        result.append(pq.pop())
    } else {
        pq.push(X)
    }
}

// Print result
print(result.map { String($0) }.joined(separator: "\n"))