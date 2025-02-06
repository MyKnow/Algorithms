// [Array<String>] S (immutable): 서로 다른 부분 문자열의 개수를 구하고자 하는 원본 문자열로 만든 배열
let S: Array<String> = (readLine() ?? "ababc").map { String($0) }

// [Set<String>] setOfDifference (mutable): 서로 다른 부분 문자열을 저장하는 집합
var setOfDifference: Set<String> = Set<String>()

for i in 0..<S.count {
    // [String] str (mutable): 문자를 조합할 때 사용할 변수
    var str = ""
    
    for j in i..<S.count {
        str += String(S[j])
        setOfDifference.insert(str)
    }
}
        
print(setOfDifference.count)