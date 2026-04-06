import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int N;
  static int[][] dp;
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    
    dp = new int[N][3];
    for (int i=0; i<N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      dp[i][0] = Integer.parseInt(st.nextToken());
      dp[i][1] = Integer.parseInt(st.nextToken());
      dp[i][2] = Integer.parseInt(st.nextToken());
    }
  }
  
  static void solve() {
    for (int i=1; i<N; i++) {
      dp[i][0] += Math.min(dp[i-1][1], dp[i-1][2]);
      dp[i][1] += Math.min(dp[i-1][0], dp[i-1][2]);
      dp[i][2] += Math.min(dp[i-1][0], dp[i-1][1]);
    }
    
    int answer = Math.min(dp[N-1][0], Math.min(dp[N-1][1], dp[N-1][2]));
    sb.append(answer).append("\n");
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}