# [def(int, int)] getGCD: 최대 공약수를 반환하는 함수
def getGCD(a, b):
    if (b==0):
        return a
    else:
        return getGCD(b, a%b)

# [def(int, int)] getLCM: 최소 공배수를 반환하는 함수
def getLCM(a, b):
    return (a*b)//getGCD(a, b)

# [int] numerator1, denominator1: 첫번째 분자와 분모 (범위(자연수): <= 30,000)
numerator1, denominator1 = map(int, input().split())

# [int] numerator2, denominator2: 두번째 분자와 분모 (범위(자연수): <= 30,000)
numerator2, denominator2 = map(int, input().split())

# [int] dOfReducedFraction: 예비 기약분수의 분모, 두 분모의 최소 공배수.
dOfReducedFraction = getLCM(denominator1, denominator2)

# [int] nOfReducedFraction: 예비 기약분수의 분자, 최소 공배수와 각 분모를 나눈 값을 분자에 곱하여 모두 더한 값
nOfReducedFraction = ((dOfReducedFraction//denominator1) * numerator1) + ((dOfReducedFraction//denominator2) * numerator2)

# [int] gcd: 기약분수로 만들기 위해서 계산한 예비 분모, 분자의 최대 공약수
gcd = getGCD(dOfReducedFraction, nOfReducedFraction)

# 예비 기약분수의 분자와 분모를 gcd로 나누어 기약분수로 만들어 출력
print(f"{nOfReducedFraction//gcd} {dOfReducedFraction//gcd}")