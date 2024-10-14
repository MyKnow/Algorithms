let inputArray: [Int] = (readLine() ?? "0 0").split(separator: " ").map{ Int($0) ?? 0 }

// 0 <= H <= 23, 불필요한 0은 제외하고 출력
// 0 <= M <= 59, 불필요한 0은 제외하고 출력

let H: Int = inputArray[0]
let M: Int = inputArray[1]

// 조정 값을 저장 할 변수 선언 및 0으로 초기화
var calcH: Int = 0
var calcM: Int = 0

// 일찍 일어 날 시간 변수
let adjustM = 45

// 분 계산
if (M < adjustM) {
    // 일찍 일어 날 시간이 입력된 시간보다 크다면 시간 계산도 필요함
    calcH = -1
    calcM = 60 + M - adjustM
} else {
    // 그렇지 않다면 분 계산만 진행함
    calcM = M - adjustM
}

// 시간 계산
if (calcH == -1) {
    // 시간 계산이 필요한 경우 날짜 변경이 필요한 지 확인함
    if (H == 0) {
        // 날짜 변경이 필요하다면 23시로 변경함
        calcH = 23
    } else {
        // 그렇지 않다면 입력된 시간에 -1을 더함
        calcH += H
    }
} else {
    // 시간 계산이 필요 없다면 입력된 시간을 사용
    calcH = H
}

print(String(calcH), String(calcM))