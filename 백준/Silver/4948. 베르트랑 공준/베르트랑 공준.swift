import Foundation

// [func(int) -> Array<Int>] getPrimeNumberArray: 2부터 목표까지의 소수를 찾아서 배열로 반환하는 함수
func getPrimeNumberArray(_ target: Int) -> Array<Int> {
    // [Int] sqrtOfTarget(immutable): target의 제곱근
    let sqrtOfTarget: Int = Int(Double(target+1).squareRoot())
    
    // [Array<Bool>] arrayOfPNs(mutable): 소수를 판별하기 위한 배열 (길이: target+1)
    var arrayOfPNs: Array<Bool> = [Bool](repeating: true, count: target+1)
    
    // 2부터 sqrtOfTarget까지 반복한다.
    for index in 2...sqrtOfTarget {
        // 만약 arrayOfPNs[index]가 true라면, index는 소수라는 뜻이다.
        // 따라서, index의 배수에 해당하는 요소들을 모두 false로 바꾼다.
        if (arrayOfPNs[index]) {
            var t: Int = 2
            
            while (t * index <= target) {
                arrayOfPNs[t*index] = false
                t += 1
            }
        } 
    }
    
    // 위 반복문을 마치고 나면, arrayOfPNs에서 값이 true인 인덱스는 소수다.
    // 따라서 값이 true인 인덱스를 배열에 차례대로 저장하여 반환한다.
    // 이 때, 0과 1은 소수가 아니므로 제외하여 저장한다.
    return arrayOfPNs.enumerated().filter { $0.offset >= 2 && $0.element }.map { $0.offset }
}

// [func(Array<Int>, Int) -> Index] findIndex: 목표의 인덱스를 반환하는 함수
func findIndex(of target: Int, in data: Array<Int>) -> Int {
    // [Int] left (mutable): 이진 탐색의 왼쪽 인덱스
    var left: Int = 0
    // [Int] right (mutable): 이진 탐색의 오른쪽 인덱스
    var right: Int = data.count - 1

    // left가 right보다 커지거나 같아지면 종료한다.
    while (left <= right) {
        // [Int] mid (immutable): 이진 탐색의 가운데 인덱스
        let mid: Int = (left+right) / 2

        // 목표가 mid번째 요소보다 작다면 right를 mid 전의 위치로 옮김
        if (target < data[mid]) {
            right = mid - 1
        }
        // 목표가 mid 또는 뒤에 있다면 left를 mid 다음자리로 옮김
        else {
            left = mid + 1
        }
    }

    // left를 반환함 (목표보다 큰 요소의 index)
    return left
}

// [Array<Int>] arrayOfN (mutable): 입력 받은 n들을 저장하는 배열
var arrayOfN: Array<Int> = [Int]()

// [Int] n(immutable): 각 테스트 케이스에서 소수를 구하는 범위 (범위: 1 ≤ n ≤ 123,456)
while let n = Int(readLine() ?? "1"), n != 0 {
    // n이 0이 아니라면 배열에 더한다.
    arrayOfN.append(n)
}

// [Array<Int>] arrayOfPrimeNumbers (mutable): 범위 내의 소수를 저장하는 배열
var arrayOfPrimeNumbers: Array<Int> = [Int]()

// arrayOfN의 최대값을 기반으로 소수 범위를 제한함.
if let maxOfN = arrayOfN.max() {
    // getPrimeNumberArray 함수를 통해 arrayOfPrimeNumbers를 업데이트
    arrayOfPrimeNumbers = getPrimeNumberArray(maxOfN * 2)
}

// [Array<Int>] arrayOfResult(mutable): 각 테스트케이스의 결과를 저장하는 배열
var arrayOfResult: Array<Int> = [Int]()

// arrayOfN를 순회하며 각 테스트 케이스에서의 정답을 배열에 저장함.
for n in arrayOfN {
    // arrayOfPrimeNumbers 속 n과 2n의 인덱스를 구하고, 둘을 빼면 개수가 산출됨.
    // 시간복잡도가 n인 firstIndex(of:) 대신, 이진 탐색 함수를 구현함.
    
    // [Int] indexOfN, indexOf2N(immutable): n과 2n의 인덱스
    let indexOfN: Int = findIndex(of: n, in: arrayOfPrimeNumbers)
    let indexOf2N: Int = findIndex(of: n * 2, in: arrayOfPrimeNumbers)
    
    // 두 index의 차를 배열에 append함.
    arrayOfResult.append(indexOf2N - indexOfN)
}

// arrayOfResult를 포맷에 맞게 한 번에 출력
print(arrayOfResult.map { String($0) }.joined(separator: "\n"))