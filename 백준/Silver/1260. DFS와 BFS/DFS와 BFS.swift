struct Stack {
    private var arr = [Int]()
    public var isEmpty: Bool { arr.isEmpty }

    mutating func push(_ val: Int) {
        arr.append(val)
    }

    mutating func pop() -> Int? {
        return arr.popLast()
    }
}

struct Queue {
    private var arr = [Int]()
    private var left: Int = 0
    public var isEmpty: Bool { arr.isEmpty || (left == arr.count) }

    mutating func push(_ val: Int) {
        arr.append(val)
    }

    mutating func pop() -> Int? {
        if isEmpty { return nil }
        defer { left += 1 }
        return arr[left]
    }
}

func dfs(_ edges: [[Int]], _ start: Int) {
    var stack = Stack()
    stack.push(start)

    var visited = [Bool](
        repeating: false,
        count: edges.count
    )

    var result = [Int]()
    while let current = stack.pop() {
        if !visited[current] {
            visited[current] = true
            result.append(current)

            for adj in edges[current].sorted(by: >) { 
                if !visited[adj] {
                    stack.push(adj)
                }
            }
        }
    }
    print(result.map { String($0) }.joined(separator: " "))
}

func bfs(_ edges: [[Int]], _ start: Int) {
    var queue = Queue()
    queue.push(start)

    var visited = [Bool](
        repeating: false,
        count: edges.count
    )
    visited[start] = true

    var result = [start]
    while let current = queue.pop() {
        for adj in edges[current].sorted(by: <) {
            if !visited[adj] {
                queue.push(adj)
                visited[adj] = true
                result.append(adj)
            }
        }
    }
    print(result.map { String($0) }.joined(separator: " "))
}

func solution() {
    guard let inputOfNMV: String = readLine() else { return }
    let arrayOfNMV: [Int] = inputOfNMV.split(separator: " ").compactMap { Int($0) }
    let (N, M, V): (Int, Int, Int) = (arrayOfNMV[0], arrayOfNMV[1], arrayOfNMV[2])

    var edges = [[Int]](
        repeating: [Int](),
        count: N+1
    )
    for _ in 0..<M {
        guard let line: String = readLine() else { return }
        let arrayOfE: [Int] = line.split(separator: " ").compactMap { Int($0) }
        let (e1, e2): (Int, Int) = (arrayOfE[0], arrayOfE[1])

        edges[e1].append(e2)
        edges[e2].append(e1)
    }

    dfs(edges, V)
    bfs(edges, V)
}

solution()