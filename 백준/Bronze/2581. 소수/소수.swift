// [Int] M (immutable): 1 이상, N 이하의 자연수
let M: Int = Int(readLine() ?? "1") ?? 1

// [Int] N: M 이상, 10,000 이하의 자연수
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] arrayOfPrime (mutable): 찾은 소수를 저장하는 배열
var arrayOfPrime: Array<Int> = [Int]()

// M에서 N 사이에 있는 소수를 찾는다.
for number in M...N {
    // 만약 주어진 수가 1 이하라면 소수가 아니므로 넘어간다.
    if (number < 2) {
        continue
    }
        
    // n으로 나누어 떨어지는 수가 없다면 number를 리스트에 추가한다.
    var isPrime: Bool = true
    for n in 2..<number {
        if (number % n == 0) {
            isPrime = false
            break
        }
    }
    if (isPrime) {
        arrayOfPrime.append(number)
    }
   
}    

// 만약 소수가 없다면 -1만 출력한다.
if (arrayOfPrime.count == 0) {
    print(-1)
}
else {
    // arrayOfPrime의 합계 출력
    print(arrayOfPrime.reduce(0, +))

    // arrayOfPrime의 최솟값 출력
    if let minValue = arrayOfPrime.min() {
        print(minValue)
    }
}