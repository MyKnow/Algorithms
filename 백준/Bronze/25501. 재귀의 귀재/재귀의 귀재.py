import sys

input = sys.stdin.readline

# [def(str, int, int, int) -> (int, int)] isPalindrome: 해당 문자열이 팰린드롬이면 1, 아니면 0을 반환하는 함수.
def isPalindrome(string, leftIndex, rightIndex, count):
    # 1. 탐색이 종료되면 1을 반환한다.
    if (leftIndex >= rightIndex):
        return (1, count)
    # 2. 문자열의 좌우가 서로 다르면 0을 반환한다.
    elif(string[leftIndex] != string[rightIndex]):
        return (0, count)
    # 3. 문자열의 좌우가 같으면 다음 인덱스를 탐색한다.
    else:
        return isPalindrome(string, leftIndex+1, rightIndex-1, count+1)

# [int] T: 테스트 케이스의 개수 (범위(자연수): 1 <= T <= 1,000)
T = int(input())

# [list(str)] result: 각 테스트 케이스에 해당하는 문자열을 저장한 리스트 (길이: T)
result = list()

for _ in range(T):
    S = input().strip()
    count = 0
    
    torf, count = isPalindrome(S, 0, len(S)-1, 1)
    
    result.append(f"{torf} {count}")
    
print("\n".join(result))