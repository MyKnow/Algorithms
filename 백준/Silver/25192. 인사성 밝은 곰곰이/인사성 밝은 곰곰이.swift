// [Int] N (immutable): 채팅방의 기록 수 (범위(자연수): 1 <= N <= 100,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Set<Strig>] person (mutable): 각 ENTER 이후로 채팅을 친 유저의 집합
// 문자열 길이: 1 <= len <= 20
var person: Set<String> = Set<String>()

// [Int] count (mutable): 이모티콘이 사용된 횟수 (초기값: 0)
var count: Int = 0

for _ in 0..<N {
    // [String] log (immutable): 채팅방 로그
    if let log: String = readLine() {  
        // 새로운 사람이 입장했다면 person을 초기화함.
        if (log == "ENTER") {
            person = Set<String>()
        }
        // 그 외의 경우 채팅을 입력한 유저의 닉네임임.
        else {
            // 집합에 없는 닉네임인 경우, 집합에 추가하고 count를 증가시킴.
            if (person.contains(log) == false) {
                person.insert(log)
                count+=1
            }
        }
    }
}

// 한 번에 출력
print(count)