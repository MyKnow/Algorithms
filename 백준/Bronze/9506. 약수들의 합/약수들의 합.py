while(True):
    #[int] n: 완전수 여부를 파악할 자연수 (범위: 2 < n < 100,000)
    n = int(input())
    
    # -1이 입력되면 반복문을 종료한다.
    if (n == -1) :
        break

    #[list(int)] factorsList: n을 제외한 n의 약수를 저장하는 리스트
    factorsList = []

    # n을 제외해야 하기 때문에 range의 범위를 1부터 n-1로 지정한다.
    for number in range(1, n):
        # number가 N의 약수인 경우 리스트에 추가한다.
        if (n % number == 0):
            factorsList.append(number)
            
    #[int] sumOfFactors: 약수들의 합을 저장하는 변수
    sumOfFactors = sum(factorsList)
    
    # 만약 완전수라면 지정된 출력에 맞춰 출력한다.
    if (n == sumOfFactors):
        print(f"{n} = " + " + ".join(map(str, factorsList)))
    else :
        print(f"{n} is NOT perfect.")