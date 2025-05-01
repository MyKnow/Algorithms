struct PriorityQueue {
    private var heap = [Int]()

    var isEmpty: Bool { heap.isEmpty }

    // Max-heap push
    mutating func push(_ value: Int) {
        heap.append(value)
        
        var idx: Int = heap.count - 1
        while idx > 0 {
            // parent node index of "idx"th node
            let prt: Int = (idx - 1) / 2

            // Max-heap: Swap between parent and child node when child node is larger than parent node
            if heap[prt] >= heap[idx] {
                break
            }
            heap.swapAt(idx, prt)

            // Retry based on parent node
            idx = prt
        }
    }

    // Max-heap pop
    mutating func pop() -> Int {
        guard !heap.isEmpty else { 
          return 0 
        }

        if heap.count == 1 {
            return heap.removeFirst()
        }

        // Saving value of top node (Maximum value)
        let top: Int = heap[0]

        // Start sorting
        heap[0] = heap.removeLast()
        
        var idx: Int = 0
        while true {
            // Index of left child node
            let left: Int = idx * 2 + 1
            
            // Index of right child node
            let right: Int = left + 1

            // Index of the node, which is the larger value 
            // between left and child node
            var maxIdx: Int = idx

            // Update maxIdx to the index of a larger node
            // either left or right
            if (left < heap.count) && (heap[left] > heap[maxIdx]) {
                maxIdx = left
            }
            if (right < heap.count) && (heap[right] > heap[maxIdx]) {
                maxIdx = right
            }

            // Break loop
            if maxIdx == idx {
                break
            }

            // Swap node
            heap.swapAt(idx, maxIdx)

            // Retry based on child node
            idx = maxIdx
        }

        return top
    }
}

let _ = readLine()

var pq = PriorityQueue()

var result = [Int]()
while let line: String = readLine(), let X: Int = Int(line) {
    if X == 0 {
        result.append(pq.pop())
    } else {
        pq.push(X)
    }
}

print(result.map { String($0) }.joined(separator: "\n"))