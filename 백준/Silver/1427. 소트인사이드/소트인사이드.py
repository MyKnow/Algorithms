# [int] N: 정렬하려는 자연수 (범위(자연수): <= 1,000,000,000)
N = int(input())

# 자연수를 리스트로 변환하여 내림차순 정렬하고, 출력 형식에 맞게 변환
print("".join(sorted(list(str(N)), reverse = True)))