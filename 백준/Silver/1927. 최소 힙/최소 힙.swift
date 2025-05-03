struct MinHeap {
    private var heap = [Int]()
    public var isEmpty: Bool { heap.isEmpty }

    @inline(__always)
    private func areSorted(_ parent: Int, _ child: Int) -> Bool { 
        heap[parent] < heap[child] 
    }

    mutating func push(_ value: Int) {
        heap.append( value )

        var child: Int = heap.count - 1
        while child > 0 {
            let parent: Int = (child - 1) / 2

            if areSorted(parent, child) { break }

            heap.swapAt(parent, child)

            child = parent
        }
    }

    mutating func pop() -> Int {
        if isEmpty {
            return 0
        } else if heap.count == 1 {
            return heap.removeFirst()
        }
        
        let top: Int = heap[0]
        heap[0] = heap.removeLast()

        var parent: Int = 0
        while true {
            var target: Int = parent
            let left: Int = (target * 2) + 1
            let right: Int = left + 1

            if (left < heap.count) && !areSorted(target, left) { target = left }
            if (right < heap.count) && !areSorted(target, right) { target = right }

            if parent == target { break }

            heap.swapAt(parent, target)

            parent = target
        }

        return top
    }
}

let _ = readLine()

var pq = MinHeap()

var result = [Int]()
while let line: String = readLine(), let X: Int = Int(line) {
    if X == 0 {
        result.append(pq.pop())
    } else {
        pq.push(X)
    }
}

print(result.map { String($0) }.joined(separator: "\n"))