import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int N, K;
  static int[][] items;
  static int[] dp;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());
    
    items = new int[N][2];
    for (int i=0; i<N; i++) {
      st = new StringTokenizer(br.readLine());
      items[i][0] = Integer.parseInt(st.nextToken());
      items[i][1] = Integer.parseInt(st.nextToken());
    }
    
    dp = new int[K+1];
  }
  
  static void solve() {
    for (int i=0; i<N; i++) {
      int weight = items[i][0];
      int value = items[i][1];
      
      int[] prev = dp.clone();
      
      for (int k=1; k<=K; k++) {
        if (k >= weight) {
          dp[k] = Math.max(prev[k], value + prev[k-weight]);
        } else {
          dp[k] = prev[k];
        }
      }
    }
    
    sb.append(dp[K]).append("\n");
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}