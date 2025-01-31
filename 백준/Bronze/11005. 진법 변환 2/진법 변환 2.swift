let arrayOfInput: Array<Int> = (readLine() ?? "0 2").split(separator: " ").map { Int($0) ?? 2}
// [Int] N (mutable): 10진법 수 (크기: <= 1,000,000,000)
var N: Int = arrayOfInput[0]

// [Int] B (immutable): 진법 (크기: 2 <= B <= 36)
let B: Int = arrayOfInput[1]

// [Array<String>] result (mutable): 자연수 N이 B진법으로 변환된 문자가 역순으로 저장된 배열
var result: Array<String> = Array<String>()

// N이 0이 되기 전까지 반복함
while(N != 0) {
    // [Int] remainer (immutable): N을 B로 나눈 나머지
    let remainer: Int = N % B
    
    // remainer가 10 이상이라면 문자로 변환되어야 함.
    if (remainer >= 10) {
        result.append(String(UnicodeScalar(remainer-10+65) ?? "A"))
    }
    // 아니라면 문자로 변환하여 바로 저장
    else {
        result.append(String(remainer))
    }
    
    // N을 B로 나눈 몫으로 다시 초기화
    N /= B
}

// result의 길이가 0이면 "0" 출력
if (result.count == 0) {
    print("0")
} else {
    // result를 역순으로 출력
    print(result.reversed().joined())
}