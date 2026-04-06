import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static final int MOD = 1_000_000_000;
  
  static int N;
  static long[][] dp;
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    
    dp = new long[N][10];
    for (int i=1; i<=9; i++) {
      dp[0][i] = 1;
    }
  }
  
  static void solve() {
    for (int idx=1; idx<N; idx++) {
      dp[idx][0] = dp[idx-1][1] % MOD;
      dp[idx][9] = dp[idx-1][8] % MOD;
      
      for (int number=1; number<=8; number++) {
        dp[idx][number] = (dp[idx-1][number-1] + dp[idx-1][number+1]) % MOD;
      }
    }
    
    long answer = 0;
    for (int i=0; i<=9; i++) {
      answer = (answer + dp[N-1][i]) % MOD;
    }
    
    sb.append(answer).append("\n");
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}