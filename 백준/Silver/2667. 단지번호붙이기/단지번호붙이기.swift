struct Queue {
    private var arr = [(Int, Int)]()
    private var left: Int = 0
    public var isEmpty: Bool { arr.isEmpty || (left == arr.count) }

    mutating func push(_ x: Int, _ y: Int) {
        arr.append( (x, y) )
    }

    mutating func pop() -> (Int, Int)? {
        if isEmpty { return nil }
        defer { left += 1 }
        return arr[left]
    }
}

func bfs(_ edges: inout [[Int]], _ x: Int, _ y: Int) -> Int {
    var queue = Queue()
    queue.push(x, y)
    edges[y][x] = 0

    // (x, y): top, bot, left, right
    let direction: [(Int, Int)] = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    var length: Int = 1
    while let (cx, cy) = queue.pop() {
        for (dx, dy) in direction {
            let (sx, sy) = (cx+dx, cy+dy)

            if 0 <= sx && sx < edges.count && 0 <= sy && sy < edges.count && edges[sy][sx] == 1 {
                queue.push(sx, sy)
                edges[sy][sx] = 0
                length += 1
            }
        }
    }

    return length
}

func solution() {
    guard let inputOfN: String = readLine(), let N: Int = Int(inputOfN) else { return }
    
    var edges = [[Int]](
        repeating: [Int](
            repeating: 0,
            count: N
        ),
        count: N
    )
    for y in 0..<N {
        guard let line: String = readLine() else { return }

        var x = 0
        for val in line {
            if val == "1" {
                edges[y][x] = 1
            }
            x+=1
        }
    }

    var result = [Int]()
    for y in 0..<N {
        for x in 0..<N {
            if (edges[y][x] == 1) {
                result.append(bfs(&edges, x, y))
            }
        }
    }

    print(result.count)
    print(result.sorted().map { String($0) }.joined(separator:"\n"))
}

solution()