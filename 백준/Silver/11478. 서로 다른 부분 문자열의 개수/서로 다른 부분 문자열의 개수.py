# [str] S: 서로 다른 부분 문자열의 개수를 구하고자 하는 원본 문자열
S = input()

# [set(str)] setOfDifference: 서로 다른 부분 문자열을 저장하는 집합
setOfDifference = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        setOfDifference.add(str(S[i:j+1]))
        
print(len(setOfDifference))