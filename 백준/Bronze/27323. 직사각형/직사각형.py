# stdin을 위한 sys import
import sys

# [int] A, B: 직사각형의 세로, 가로 길이 (범위: 1 <= A, B <= 100의 자연수)
A, B = map(int, sys.stdin.read().strip().split())

# 넓이 출력
print(A*B)