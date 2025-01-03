# T: int - 테스트 케이스의 개수 (1 <= T <= 10)
T = int(input())

for _ in range(T):
    # word: String - 알파벳 대문자로만 이루어진 문자열 (길이: <1000)
    word = input()
    
    print(word[0]+word[len(word)-1])