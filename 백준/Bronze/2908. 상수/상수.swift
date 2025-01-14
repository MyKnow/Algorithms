// [Array<String>] arrayOfFirstInput (immutable) : 서로 같지 않고 0을 포함하지 않는, 두 개의 세 자리 수 (길이: 2)
let arrayOfFirstInput: Array<String> = (readLine() ?? "100 100").split(separator: " ").map(String.init)

// [Array<Int>] reversedNumbers (immutable): 각 수의 문자열을 역으로 저장한 배열 (길이 : 2)
let reversedNumbers: Array<Int> = arrayOfFirstInput.map{Int(String($0.reversed()) ?? "100") ?? 100}

// [Int] bigger (immutable) : 두 수 중에서 크기가 큰 수
let bigger: Int = reversedNumbers.max() ?? 100

// 출력
print(bigger)