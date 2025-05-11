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

    // Sort adjacency array in ascending order to ensure answers
    for i in 1...N {
        edges[i].sort()
    }
    
    // visited[i]: order when node i was visited
    var visited = [Int](
        repeating: 0,
        count: N+1
    )
    var order: Int = 1
    
    // Start DFS
    dfs(&order, R, &visited, edges)
    
    // Output visit order for all nodes
    for i in 1...N {
        print(visited[i])
    }
}


func dfs(
    _ order: inout Int,
    _ v: Int,
    _ visited: inout [Int],
    _ edges: [[Int]]
) {
    visited[v] = order

    for x in edges[v] {
        if visited[x] == 0 {
            order += 1
            dfs(&order, x, &visited, edges)
        }
    }
}

solution()