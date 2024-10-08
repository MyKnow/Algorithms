var countOfZero: Int = 0
var countOfOne: Int = 0
var arr: [[Int]] = Array(repeating: Array(repeating: -1, count: 41), count: 3)

func fibonacci(n: Int) -> Int {
    if (n == 0) {
        countOfZero += 1
        return 0
    } else if (n == 1) {
        countOfOne += 1
        return 1
    } else {
        if (arr[2][n] != -1) {
            countOfZero += arr[0][n]
            countOfOne += arr[1][n]
            return arr[2][n]
        } else {
            let result = fibonacci(n: n-1) + fibonacci(n: n-2)
            arr[0][n] = countOfZero
            arr[1][n] = countOfOne
            arr[2][n] = result
            return result
        }
    }
}

let testCase: Int = Int(readLine() ?? "0") ?? 0

for _ in 0..<testCase {
    let n: Int = Int(readLine() ?? "0") ?? 0
    
    countOfZero = 0
    countOfOne = 0
    arr = Array(repeating: Array(repeating: -1, count: 41), count: 3)
    
    fibonacci(n: n)
    
    print(String(countOfZero), String(countOfOne))
}


