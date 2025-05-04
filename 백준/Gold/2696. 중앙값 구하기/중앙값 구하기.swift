struct Heap {
    private var heap = [Int]()
    private let areSorted: (Int, Int) -> Bool
    

    init(_ sort: @escaping (Int, Int) -> Bool) {
        self.areSorted = sort
    }

    public var isEmpty: Bool { heap.isEmpty }
    public var top: Int? { heap.first }
    public var length: Int { heap.count }

    @inline(__always)
    private func isOrdered(_ parent: Int, _ child: Int) -> Bool {
        return areSorted(heap[parent], heap[child])
    }

    mutating func push(_ value: Int) {
        heap.append(value)
        var child = length - 1

        while child > 0 {
            let parent = (child - 1) / 2
            if isOrdered(parent, child) { break }
            heap.swapAt(parent, child)
            child = parent
        }
    }

    mutating func pop() -> Int {
        if isEmpty { return 0 }
        if length == 1 { return heap.removeFirst() }

        let top = heap[0]
        heap[0] = heap.removeLast()
        var parent = 0

        while true {
            var target = parent
            let left = parent * 2 + 1
            let right = left + 1

            if left < length && !isOrdered(target, left) {
                target = left
            }
            if right < length && !isOrdered(target, right) {
                target = right
            }
            if parent == target { break }
            heap.swapAt(parent, target)
            parent = target
        }

        return top
    }
}

func solution() {
    guard let inputOfT = readLine(), let T = Int(inputOfT) else { return }
    
    for _ in 0..<T {
        guard let inputOfM = readLine(), let M = Int(inputOfM) else { return }
        print((M / 2) + 1)

        // MaxHeap
        var left = Heap(>)
        // MinHeap
        var right = Heap(<)
    
        var count: Int = 0
        var nums = [Int]()
        while nums.count < M {
            guard let line = readLine() else { return }
            nums.append( contentsOf: line.split(separator: " ").compactMap { Int($0) } )
        }

        var result: String = ""
        for i in 0..<M {
            let num: Int = nums[i]
            
            if let top = left.top, num <= top {
                left.push(num)
            }
            else {
                right.push(num)
            }
    
            // Balance heaps
            if left.length > right.length + 1 {
                right.push(left.pop())
            } 
            else if right.length > left.length {
                left.push(right.pop())
            }
    
            // Collect middle values (only when index is even)
            if i % 2 == 0 {
                if let top = left.top {
                    result += String(top)
                    count += 1
                    
                    if count % 10 == 0 {
                        result += "\n"
                    } else {
                        result += " "
                    }
                }
            }
        }
        
        print(result)
    }
}

solution()