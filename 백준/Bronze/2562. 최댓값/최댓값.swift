// [Array<Int>] arr : 길이가 9로 고정된 서로 다른 자연수로 구성된 배열
var arr: Array<Int> = []

// 9번 반복하여 list에 int를 append
for _ in 0..<9 {
    let number: Int = Int(readLine() ?? "0") ?? 0
    arr.append(number)
}

// [int] maxOfArray : Array의 요소 중 최대값
let maxOfArray = arr.max() ?? 0

// [int] indexOfMax : max 값이 Array에서 몇번째 인덱스인지 저장한 변수
let indexOfMax = arr.firstIndex(of: maxOfArray) ?? 0

print(maxOfArray, indexOfMax+1, separator: "\n")
