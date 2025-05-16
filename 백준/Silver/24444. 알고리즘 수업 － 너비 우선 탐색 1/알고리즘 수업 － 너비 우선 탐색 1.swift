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

func bfs(_ edges: [[Int]], _ r: Int) -> [Int] {
    var order = 1
    
    var visited = [Int](
        repeating: 0,
        count: edges.count
    )
    visited[r] = order
    
    var dq = Queue()
    dq.append(r)

    while let node = dq.popLeft() {
        for n in edges[node].sorted() {
            if (visited[n] == 0) {
                order += 1
                visited[n] = order
                dq.append(n)
            }
        }
    }

    return visited
}

func solution() {
    guard let inputOfNMR: String = readLine() else { return }
    let arrayOfNMR: [Int] = inputOfNMR.split(separator: " ").compactMap { Int($0) }
    let (N, M, R) = (arrayOfNMR[0], arrayOfNMR[1], arrayOfNMR[2])
    
    var edges = [[Int]](
        repeating: [Int](),
        count: N+1
    )
    
    for _ in 0..<M { 
        guard let inputOfUV: String = readLine() else { return }
        let arrayOfUV: [Int] = inputOfUV.split(separator: " ").compactMap { Int($0) }
        let (u, v) = (arrayOfUV[0], arrayOfUV[1])
    
        edges[u].append(v)
        edges[v].append(u)
    }
    

    print(bfs(edges, R).dropFirst().map { String($0) }.joined(separator: "\n"))
}

solution()