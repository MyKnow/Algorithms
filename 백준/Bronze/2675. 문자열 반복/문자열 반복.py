# [int] T : 테스트 케이스의 개수 (1 <= T <= 1,000)
T = int(input())

# T회 반복함
for _ in range(T):
    # [string] S : 새 문자열을 만들 때 쓸 원본 문자열 (길이 : 1 <= len < 20)
    originalR, S = input().split(" ")
    # [int] R : 문자열에서 각 문자를 반복할 횟수 (1 <= R <= 8)
    R = int(originalR)
    
    # S의 글자들을 반복문으로 인덱싱함
    for char in S :
        # 분리된 글자인 char를 R회 반복하여 출력함
        print(char*R, end="")
    
    # 모든 글자를 출력하면 개행함
    print()