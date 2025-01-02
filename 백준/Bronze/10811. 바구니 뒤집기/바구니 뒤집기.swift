let arrayOfFirstReadline: Array<Int> = (readLine() ?? "1 1").split(separator: " ").map{Int($0) ?? 1}
// N: Int (immutable) - 바구니의 개수 (1 <= N <= 100)
let N: Int = arrayOfFirstReadline[0]
// M: Int (immutable) - 바구니를 역순으로 만드는 횟수 (1 <= M <= 100)
let M: Int = arrayOfFirstReadline[1]

// bucket: Array<Int> (mutable) - 바구니 리스트 (길이: N)
var bucket: Array<Int> = Array<Int>(1...N)

// M번에 걸쳐서, 매회 i-1부터 j-1번째까지의 바구니의 순서를 역순으로 변경한다.
for _ in 0..<M {
    let arrayOfEachReadline: Array<Int> = (readLine() ?? "1 1").split(separator: " ").map{Int($0) ?? 1}
    // i: Int - 역순으로 만들 바구니 중 제일 왼쪽 (1 <= i <= j <= N)
    let i: Int = arrayOfEachReadline[0]
    // j: Int - 역순으로 만들 바구니 중 제일 오른쪽 (1 <= i <= j <= N)
    let j: Int = arrayOfEachReadline[1]
    
    // i-1부터 j-1까지의 index를 뒤집어서 저장한다.
    bucket[i-1...j-1].reverse()
}
for number in bucket {
    print(number, terminator: " ")
}