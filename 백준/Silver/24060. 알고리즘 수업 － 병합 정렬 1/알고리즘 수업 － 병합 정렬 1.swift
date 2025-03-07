// [func<inout [Int], Int, Int, Int, Int>] mergeSort
// 주어진 정수 배열을 오름차순 정렬하여, 원본 target과 count를 업데이트 하는 함수
func mergeSort(_ target: inout [Int], _ left: Int, _ right: Int, _ count: inout Int, _ limit: Int) {
    if (left < right) {
        // 배열의 중앙 Index
        let mid: Int = (left + right) / 2
        
        mergeSort(&target, left, mid, &count, limit)
        mergeSort(&target, mid + 1, right, &count, limit)
        merge(&target, left, mid, right, &count, limit)
    }
}

// [func<inout [Int], Int, Int, Int, Int] merge
// 주어진 정수 배열을 오름차순 정렬하여 병합하는 함수
func merge(_ target: inout [Int], _ left: Int, _ mid: Int, _ right: Int, _ count: inout Int, _ limit: Int) {
    // [Int] i (mutable): 왼쪽 배열의 시작 인덱스
    var i: Int = left
    // [Int] j (mutable): 오른쪽 배열의 시작 인덱스
    var j: Int = mid + 1
    // [Array<Int>] tmp (mutable): 병합에 사용할 임시 정수 배열 (길이: target.count)
    var tmp = [Int]()
    
    // 1. 왼쪽 인덱스와 오른쪽 인덱스를 증가 시키며, 오름차순 정렬 시킨다.
    while (i <= mid && j <= right) {
        if (target[i] <= target[j]) {
            tmp.append(target[i])
            i+=1
        } else {
            tmp.append(target[j])
            j+=1
        }
    }
    
    // 2. 왼쪽 배열의 원소가 남아 있을 때
    while (i <= mid) {
        tmp.append(target[i])
        i+=1
    }
    
    // 3. 오른쪽 배열의 원소가 남아 있을 때
    while (j <= right) {
        tmp.append(target[j])
        j+=1
    }
    
    // 4. 병합
    i = left
    var t = 0
    
    while (i <= right) {
        count += 1
        if (count == limit) {
            print(tmp[t])
        }
        target[i] = tmp[t]
        i+=1
        t+=1
    }
}

// [Int, Int] N, K (Immutable)
// N: 리스트 A의 크기 (범위(자연수): 5 <= N <= 500,000)
// K: 저장 횟수 (범위(자연수): 1 <= K <= 10^8)
let arrayOfInput: [Int] = (readLine() ?? "5 1").split(separator: " ").compactMap { Int($0) }
let (N, K): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

/// [Array<Int>] A (Mutable): 입력 받은 수를 저장한 배열 (길이: N)
var A: [Int] = (readLine() ?? "1").split(separator: " ").compactMap { Int($0) }

// mergeSort 실행
var count: Int = 0
mergeSort(&A, 0, N - 1, &count, K)

if (count < K) {
    print(-1)
}