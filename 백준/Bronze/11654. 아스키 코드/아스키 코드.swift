// [String] inputOfAscii (immutable) : 사용자로부터 입력받은 아스키코드를 저장하는 함수
let inputOfAscii: String = readLine() ?? "A"

// [UInt8] convertedAscii (immutable) : inputOfAscii를 Character 형으로 변환한 변수
let convertedAscii: UInt8 = Character(inputOfAscii).asciiValue ?? 0

// 입력받은 아스키코드를 숫자로 변환하여 출력한다.
print(convertedAscii)