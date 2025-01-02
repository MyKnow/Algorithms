let arrayOfFirstReadLine: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) } // 문자열을 나누고 정수로 변환

// N: Int (immutable) - 바구니의 개수 (1 <= N <= 100)
let N: Int = arrayOfFirstReadLine[0]
// M: Int (immutable) - 공을 넣을 횟수 (1 <= M <= 100)
let M: Int = arrayOfFirstReadLine[1]

// bucket: Array<Int> (mutable) - 바구니 리스트 (길이: N)
var bucket: Array<Int> = Array(repeating: 0, count: N)

// M번동안, i, j, k를 입력 받아서 bucket 수정을 반복함
for _ in 0..<M {
    let arrayOfEachReadLine = (readLine() ?? "1 1 1").split(separator: " ").compactMap { Int($0) } // 문자열을 나누고 정수로 변환
    
    // i: Int (immutable) - 공을 넣을 첫번째 바구니의 index+1 (1 <= i <= j <= N)
    let i: Int = arrayOfEachReadLine[0]
    // j: Int (immutable) - 공을 넣을 마지막 바구니의 index+1 (1 <= i <= j <= N)
    let j: Int = arrayOfEachReadLine[1]
    // k: Int (immutable) - i-1부터 j번째 바구니에 넣을 공의 번호 (1 <= k <= N)
    let k: Int = arrayOfEachReadLine[2]

    // 매 반복마다 입력 값으로 바구니를 수정함
    for index in i-1..<j {
        bucket[index] = k
    }
}

// 모든 수정이 종료되면, 각 바구니의 값을 출력함
for number in bucket {
    print(number, terminator: " ")
}