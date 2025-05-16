struct Queue {
    private var queue = [Int]()
    private var left = 0

    mutating func popLeft() -> Int? {
        guard left < queue.count else { return nil }
        defer { left += 1 }
        return queue[left]
    }

    mutating func append(_ val: Int) {
        queue.append(val)
    }
}

func bfs(_ edges: [[Int]], _ r: Int) -> Int {
    var total = -1
    
    var visited = [Bool](
        repeating: false,
        count: edges.count + 1
    )
    
    var dq = Queue()
    dq.append(r)

    while let node = dq.popLeft() {
        for n in edges[node].sorted(by: >) {
            if (!visited[n]) {
                visited[n] = true
                total += 1
                dq.append(n)
            }
        }
    }

    return max(0, total)
}

func solution() {
    guard let inputOfC: String = readLine(), let C = Int(inputOfC) else { return }
    guard let inputOfP: String = readLine(), let P = Int(inputOfP) else { return }
    
    var edges = [[Int]](
        repeating: [Int](),
        count: C+1
    )
    
    for _ in 0..<P { 
        guard let inputOfUV: String = readLine() else { return }
        let arrayOfUV: [Int] = inputOfUV.split(separator: " ").compactMap { Int($0) }
        let (u, v) = (arrayOfUV[0], arrayOfUV[1])
    
        edges[u].append(v)
        edges[v].append(u)
    }
    

    print(bfs(edges, 1))
}

solution()