# [(int, int)] N, B: 10진법 수 N, B진법
# 1 <= N <= 1,000,000,000
# 2 <= B <= 36
N, B = map(int, input().split())

# [list] result: B진법으로 변환된 N을 담은 list
result = []

# N을 B로 나눈 나머지 -> 변환된 값
# N이 0 아닌 경우 계속 계산을 이어 가야 함.
while (N != 0) :
    # [int] remainer: N을 B로 나눈 나머지
    remainer = N % B
    
    # 나머지가 10 이상이라면 알파벳으로 변환해야 함
    if (remainer >= 10) :
        result.append(chr(remainer-10+ord("A")))
    # 숫자인 경우 숫자를 str로 변환하여 더함
    else :
        result.append(str(remainer))
        
    # N을 B로 나눈 몫으로 초기화
    N//=B
    
# result를 역으로 출력하되, 0인 경우 "0"을 출력하게 예외처리
print("".join(result[::-1]) if len(result) > 0 else "0")