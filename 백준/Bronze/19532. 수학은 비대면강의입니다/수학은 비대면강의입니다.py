# [int] a, b, c, d, e, f: 연립방정식의 계수 (범위(정수): -999 <= ... <= 999)
a, b, c, d, e, f = map(int, input().split())

# 아래 연립방정식을 만족하는 (x, y)가 유일하게 존재한다.
# 이 때 (x, y)의 범위는 -999 이상 999 이하의 정수임이 보장된다.
# ax + by = c
# dx + ey = f
# 
# 행렬식을 통해서 연립 방정식의 해를 구한다.
# [int] D: a*e-b*d
D = (a * e) - (b * d)
# [int] Dx: (c * e) - (b * f)
Dx = (c * e) - (b * f)
# [int] Dy: (a * f) - (c * d)
Dy = (a * f) - (c * d)

# D가 0이 아니면 유일한 해가 존재함.
if (D != 0): 
    print(f"{Dx//D} {Dy//D}")
# 문제 상에서 해가 항상 존재한다고 했으므로, 해가 없는 예외처리는 구현하지 않음
else :
    pass