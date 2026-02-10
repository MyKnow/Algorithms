import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int T;
  static int N, X, M;
  
  static int[] cages;
  static int[] best;
  static int[][] cond;
  
  static int maxSum;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    X = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    
    cages = new int[N];
    best = null;
    cond = new int[M][3];
    
    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      cond[i][0] = Integer.parseInt(st.nextToken()) - 1;
      cond[i][1] = Integer.parseInt(st.nextToken()) - 1;
      cond[i][2] = Integer.parseInt(st.nextToken());
    }
    
    maxSum = -1;
  }
  
  static void dfs(int idx, int curSum) {
    // 최대합 가지치기
    if (curSum + (N - idx) * X <= maxSum) return;
    
    if (idx == N) {
      if (checkAll()) {
        if (curSum > maxSum) {
          maxSum = curSum;
          best = cages.clone();
        }
      }
      return;
    }
    
    for (int v = 0; v <= X; v++) {
      cages[idx] = v;
      if (isPossible(idx)) {
        dfs(idx + 1, curSum + v);
      }
    }
  }
  
  static boolean isPossible(int idx) {
    for (int i = 0; i < M; i++) {
      int l = cond[i][0];
      int r = cond[i][1];
      int s = cond[i][2];
      
      int sum = 0;
      int filled = 0;
      
      for (int j = l; j <= r; j++) {
        if (!(j < idx && idx <= r)) break;
        sum += cages[j];
        filled++;
      }
      
      int remain = (r - l + 1) - filled;
      
      if (sum > s) return false;
      if (sum + remain * X < s) return false;
    }
    return true;
  }
  
  static boolean checkAll() {
    for (int i = 0; i < M; i++) {
      int l = cond[i][0];
      int r = cond[i][1];
      int s = cond[i][2];
      
      int sum = 0;
      for (int j = l; j <= r; j++) {
        sum += cages[j];
      }
      if (sum != s) return false;
    }
    return true;
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t <= T; t++) {
      init();
      dfs(0, 0);
      
      sb.append("#").append(t).append(" ");
      if (maxSum == -1) {
        sb.append("-1");
      } else {
        for (int i = 0; i < N; i++) {
          sb.append(best[i]).append(" ");
        }
      }
      sb.append("\n");
    }
    System.out.print(sb.toString());
  }
}