import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T;
  
  static int N, B;
  static int answer;
  static int[] height;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    B = Integer.parseInt(st.nextToken());
    
    height = new int[N];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      height[i] = Integer.parseInt(st.nextToken());
    }
    
    answer = Integer.MAX_VALUE;
  }
  
  static void dfs(int idx, int sum) {
    if (sum >= B) {
      answer = Math.min(answer, sum - B);
      return;
    }
    
    if (idx == N) return;
    
    // 선택
    dfs(idx + 1, sum + height[idx]);
    
    // 미선택
    dfs(idx + 1, sum);
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t <= T; t++) {
      init();
      dfs(0, 0);
      sb.append("#").append(t).append(" ").append(answer).append("\n");
    }
    System.out.print(sb.toString());
  }
}
