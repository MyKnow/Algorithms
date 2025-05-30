func bfs(_ field: inout [[Int]], _ points: inout Set<[Int]>) -> Int {
    let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    var worm = 0

    while let first = points.first {
        worm += 1
        points.remove(first)
    
        var stack = [first]

        while let current = stack.popLast() {
            let (cx, cy) = (current[0], current[1])
            field[cy][cx] = 0
            points.remove( current )
            
            for (x, y) in directions {
                let dx = cx+x
                let dy = cy+y
                
                if (0 <= dy && dy < field.count) && (0 <= dx && dx < field[0].count) && (field[dy][dx] == 1) {
                    if points.contains( [dx, dy] ) {
                        stack.append( [dx, dy] )
                    }
                }
            }
        }
    }

    return worm
    
}
    
func solution() {
    guard let inputOfT = readLine(), let T: Int = Int(inputOfT) else { return }
    
    for _ in 0..<T {
        guard let inputOfMNK = readLine() else { return }
        let arrayOfMNK = inputOfMNK.split(separator: " ").compactMap { Int($0) }
        let (M, N, K) = (arrayOfMNK[0], arrayOfMNK[1], arrayOfMNK[2])
    
        var field = [[Int]](
            repeating: [Int](
                repeating: 0,
                count: M
            ),
            count: N
        )
        
        var points = Set<[Int]>()
        for _ in 0..<K {
            guard let inputOfXY = readLine() else { return }
            let arrayOfXY = inputOfXY.split(separator: " ").compactMap { Int($0) }
            points.insert( arrayOfXY )
            field[arrayOfXY[1]][arrayOfXY[0]] = 1
        }
    
        print(bfs(&field, &points))  
    }  
}

solution()