let inputArray: [Int] = (readLine() ?? "0 0").split(separator: " ").map{ Int($0) ?? 0}

// 0 <= A <= 23, 현재 시각의 시, 불필요한 10의 자리의 0은 고려하지 않음
// 0 <= B <= 59, 현재 시각의 분, 불필요한 10의 자리의 0은 고려하지 않음
let A: Int = inputArray[0]
let B: Int = inputArray[1]

// 0 <= C <= 1000, 요리하는 데 필요한 시간, 분 단위
let C: Int = Int(readLine() ?? "0") ?? 0

// calcH : C에 의해 더해질 시 값을 저장하는 변수
let calcH: Int = (B+C) / 60

// resultH : 계산이 완료된 시 값을 저장하는 변수
// resultM : C에 의해 더해진 분 값을 형식에 맞춰 저장한 변수
var resultH : Int = 0
let resultM: Int = (B+C) % 60

// 시간 조정이 필요한 경우
if (calcH > 0) {
    // 결과가 23시를 넘길 경우 재계산이 필요함
    if ((A + calcH) / 24 > 0) {
        resultH = (A + calcH) % 24
    } else {
        // 그렇지 않은 경우 더하기만 진행함
        resultH = A + calcH
    }
} else {
    // 시간 조정이 불필요한 경우, A로 초기화
    resultH = A
}

print(String(resultH), String(resultM))