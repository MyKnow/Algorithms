import Foundation

var sudoku = [[Int]]()
var blank = [[Int]]()

// 입력 받기
for _ in 0..<9 {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    sudoku.append(input)
}

// 빈칸 조사
for i in 0..<9 {
    for j in 0..<9 {
        if sudoku[i][j] == 0 {
            blank.append([i, j])
        }
    }
}

// 가로, 세로 줄 판별
func line(_ n: Int, _ i: Int, _ j: Int) -> Bool {
    for k in 0..<9 {
        if sudoku[i][k] == n || sudoku[k][j] == n {
            return false
        }
    }
    
    return true
}

// 사각형 판별
func square(_ n: Int, _ i: Int, _ j: Int) -> Bool {
    for k in 0..<3 {
        for l in 0..<3 {
            if sudoku[i/3*3+k][j/3*3+l] == n {
                return false
            }
        }
    }
    
    return true
}

// 스도쿠 채우기
func dfs(_ depth: Int) {
    if depth == blank.count {
        for line in sudoku {
            print(line.map { String($0) }.joined(separator: " "))
        }
        exit(0)
    }
    
    for i in 1...9 {
        let y = blank[depth][0]
        let x = blank[depth][1]
        
        if line(i, y, x) && square(i, y, x) {
            sudoku[y][x] = i
            dfs(depth+1)
            sudoku[y][x] = 0
        }
    }
}

dfs(0)