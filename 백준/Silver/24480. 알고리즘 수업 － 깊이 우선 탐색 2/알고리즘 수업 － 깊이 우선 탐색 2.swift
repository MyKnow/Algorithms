func solution() {
    guard let inputOfNMR = readLine() else { return }
    let arrayOfNMR: [Int] = inputOfNMR.split(separator: " ").compactMap { Int($0) }
                                                                        
    // N: number of nodes
    // M: number of edges
    // R: start node
    let (N, M, R) = (arrayOfNMR[0], arrayOfNMR[1], arrayOfNMR[2])

    // edges[i]: 2-Dimensional array of adjacent nodes of node i
    var edges = [[Int]](
        repeating: [Int](),
        count: N+1
    )
                                                                         
    for _ in 0..<M {
        guard let inputOfUV = readLine() else { return }
        let arrayOfUV: [Int] = inputOfUV.split(separator: " ").compactMap { Int($0) }
        let (u, v) = (arrayOfUV[0], arrayOfUV[1])
        edges[u].append(v)
        edges[v].append(u)
    }
    
    // Start DFS
    print(dfs(R, &edges).map { String($0) }.joined(separator: "\n"))
}


func dfs(
    _ v: Int,
    _ edges: inout [[Int]]
) -> [Int] {
    var visited = [Int](
        repeating: 0,
        count: edges.count
    )
    var order: Int = 1
    var stack: [Int] = [v]

    while !stack.isEmpty {
        let edge: Int = stack.removeLast()

        if visited[edge] == 0 {
            visited[edge] = order
            order += 1

            for x in edges[edge].sorted() {
                if visited[x] == 0 {
                    stack.append(x)
                }
            }
        }
    }

    visited.removeFirst()
    
    return visited
}

solution()