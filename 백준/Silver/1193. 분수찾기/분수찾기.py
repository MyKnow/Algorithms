# [int] X: 구해야 하는 분수의 index (범위 : 1 <= X <= 10,000,000)
X = int(input())

# [int] nowNumber: 현재 X의 라인 내 위치
nowNumber = X

# [int] index: X번째 분수가 속해있는 index
index = 1

# 무작정 while문으로 처음부터 구하려고 하면 X값이 커서 시간초과가 발생한다.
# while문을 통해서 X번째 분수가 속해있는 대각선 index를 구한다.
# nowNumber에서 현재 index에 해당하는 수를 빼면, 결국 마지막 반복문에서 X가 있는 index 내에서의 위치가 남을 것이다.
# index를 계속 증가시키면서, 더 이상 뺄 수 없을 때 반복문을 종료 시키도록 한다.
while(nowNumber > index):
    nowNumber -= index
    index += 1

# 짝수번째 index는 분모가 줄어드는 패턴이고, 홀수번째 index는 분자가 줄어드는 패턴이다.
if (index % 2 == 0) :
    print(f"{nowNumber}/{(index-nowNumber+1)}")
else :
    print(f"{(index-nowNumber+1)}/{nowNumber}")