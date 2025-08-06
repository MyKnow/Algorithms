def solution(n, money):
    MOD = 1_000_000_007
    
    # dp[n]: n원을 만드는 방법의 수
    dp = [0] * (n+1)
    # 0원을 만드는 방법은 "동전을 사용하지 않는 경우"인 1가지
    dp[0] = 1
    
    for coin in money:
        # coin을 사용해서 coin부터 n원까지 만드는 경우의 수 각각을 dp에 저장함
        for i in range(coin, n+1):
            # prev: 이전까지의 i원을 만드는 경우의 수
            prev = dp[i]
            
            # crt: i - coin 원을 만들 수 있는 모든 방법에 coin 하나를 추가해서 i원을 만들 수 있음
            crt = dp[i-coin]
            
            dp[i] = (prev+crt) % MOD
            
    return dp[n]