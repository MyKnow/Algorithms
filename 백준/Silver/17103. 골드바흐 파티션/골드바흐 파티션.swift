import Foundation

// [func(Int) -> Array<Int>] getPrimeNumbers: 2부터 target까지의 범위에 해당하는 소수 배열을 반환하는 함수
func getPrimeNumbers(of target: Int) -> Array<Int> {
    // [Int] sqrtTarget (immutable): target의 제곱근
    let sqrtTarget: Int = Int(Double(target).squareRoot())
    
    // [Array<Bool>] arrayOfPN (mutable): 인덱스가 소수일 때 값이 true인 배열 (길이: target+1)
    var arrayOfPN: Array<Bool> = [Bool](repeating: true, count: target+1)
    
    // 0, 1은 소수가 아님.
    arrayOfPN[0] = false
    arrayOfPN[1] = false

    // 2부터 sqrtTarget까지 순회하며 arrayOfPN을 업데이트한다.
    for index in 2...sqrtTarget {
        // 만약 arrayOfPN[index]가 true라면 index는 소수이다.
        // 따라서, index의 배수들은 소수가 아니다.
        if (arrayOfPN[index]) {
            // index의 배수를 모두 false로 업데이트한다.
            // 최적화를 위해 index*index부터 시작한다.
            // target을 포함해서 수정해야 하므로 target까지 반복한다.
            // index의 배수를 업데이트 하므로 index 간격으로 반복한다.
            // index의 배수를 모두 False로 변경한다.
            for mul in stride(from: index*index, through: target, by: index) {
                arrayOfPN[mul] = false
            }
        }
    }
    
    // 수정이 종료되면 element가 true인 offset만을 추출하여 배열로 만들고 반환한다.
    return arrayOfPN.enumerated().compactMap { $0.element ? $0.offset : nil}
}

// [Int] T (immutable): 테스트 케이스의 개수 (범위(자연수): 1 ≤ T ≤ 100)
let T: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] arrayOfN (mutable): 각 테스트 케이스의 N을 저장한 배열 (길이: T)
var arrayOfN: Array<Int> = [Int]()

for _ in 0..<T {
    // 골드바흐 파티션의 개수를 구할 짝수 (범위(자연수): 2 < N ≤ 1,000,000)
    if let N = Int(readLine() ?? "1") {
        arrayOfN.append(N)
    }
}

// [Int] maxOfN (immutable): arrayOfN에서 가장 큰 수
let maxOfN: Int = arrayOfN.max() ?? 1
    
// [Array<Int>] arrayOfPN (immutable): 2부터 arrayOfN의 max값까지의 범위에 해당하는 소수 배열
let arrayOfPN: Array<Int> = getPrimeNumbers(of: maxOfN)

// [Set<Int>] setOfPN: arrayOfPN의 집합
let setOfPN: Set<Int> = Set(arrayOfPN)

// [Array<Int>] arrayOfCounts (mutable): 각 테스트케이스 N에 대해서 발견한 골드바흐 파티션의 개수를 저장하는 배열
var arrayOfCounts: Array<Int> = [Int]()

// arrayOfN을 순회하며 arrayOfCounts를 업데이트 한다.
for n in arrayOfN {
    // [Int] count (mutable): n의 골드바흐 파티션 개수
    var count: Int = 0
    
    
    for pn in arrayOfPN {
        //소수가 목표 짝수의 절반보다 커지면 종료한다.
        if ((n/2) < pn) {
            break
        }
            
        // 현재 목표 짝수 n과 소수 pn에 대해서, n-pn이 setOfPN 안에 존재한다면 count를 증가시킨다.
        if (setOfPN.contains(n-pn)) {
            count += 1
        }
    }
    
    // arrayOfCounts에 현재 count를 추가한다.
    arrayOfCounts.append(count)
}
    
// arrayOfCounts를 형식에 맞게 출력한다.
print(arrayOfCounts.map { String($0) }.joined(separator: "\n"))