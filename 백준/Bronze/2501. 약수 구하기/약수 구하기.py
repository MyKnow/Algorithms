#[(int, int)] N, K: 약수 관계를 파악할 두 자연수 (범위: 1 <= K <= N <= 10,000)
N, K = map(int, input().split())

#[list(int)] factorsList: N의 약수를 저장하는 리스트
factorsList = []

for number in range(1, N+1):
    # number가 N의 약수인 경우 리스트에 추가한다.
    if (N % number == 0):
        factorsList.append(number)

# factorsList의 길이가 K보다 작다면 0을 출력한다.
print(0 if (len(factorsList) < K) else factorsList[K-1])