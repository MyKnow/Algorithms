let arrayOfFirstReadLine: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap{Int($0)}
// N: Int (immutable) - 가지고 있는 바구니의 개수 (1 <= N <= 100)
let N: Int = arrayOfFirstReadLine[0]
// M: Int (immutable) - 공을 바꾸려는 횟수 (1 <= M <= 100)
let M: Int = arrayOfFirstReadLine[1]
        
// bucket: Array<Int> (mutable) - 공이 들어있는 바구니의 Int 배열 (길이: N)
var bucket: Array<Int> = [Int](1...N)
    
// 각 반복마다 i와 j번째 바구니에 들어있는 공을 서로 교환한다.
for _ in 0..<M {
    let arrayOfEachReadLine: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap{Int($0)}
    
    // i: Int (immutable) - 공을 교환할 바구니 중 첫번째 ( 1 <= i <= j <= N)
    let i: Int = arrayOfEachReadLine[0]
    // j: Int (immutable) - 공을 교환할 바구니 중 두번째 ( 1 <= i <= j <= N)
    let j: Int = arrayOfEachReadLine[1]
            
    // k: Int (immutable) - 공을 교환하기 위해서 사용하는 임시 바구니
    let k: Int = bucket[i-1]
        
    // i-1번째 바구니에 j-1번째 바구니의 공을 넣는다.
    bucket[i-1] = bucket[j-1]
    
    // j-1번째 바구니에 임시 바구니의 공을 넣는다.
    bucket[j-1] = k
}

// 공을 모두 다 교환하면 각 바구니의 공을 출력한다.
for number in bucket {
    print(number, terminator: " ")
}