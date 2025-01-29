// replacingOccurrences 메서드를 사용하기 위해 Foundation을 import
import Foundation

// [String] croatiaString (mutable) : 크로아티아 알파벳이 포함되어 있을 수도 있는 문자열 (길이: 최대 100 단어)
var croatiaString: String = readLine() ?? "a"

// [Array<String>] croatiaTable (immutable) : 크로아티아 알파벳을 정리해놓은 리스트
let croatiaTable: Array<String> = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

// 크로아티아 알파벳을 전부 '*' 한 글자로 치환함.
for croatiaAlphabet in croatiaTable {
    croatiaString = croatiaString.replacingOccurrences(of: croatiaAlphabet, with: "*")
}
        
// *이 추가된 croatiaString의 길이를 더한 값을 출력한다.
print(croatiaString.count)