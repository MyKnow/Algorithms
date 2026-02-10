import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int N;
  static int count;
  
  // 열, 대각선 점유 여부
  static boolean[] col;
  static boolean[] diag1; // row - col + N
  static boolean[] diag2; // row + col
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    
    col = new boolean[N + 1];
    diag1 = new boolean[2 * N + 1];
    diag2 = new boolean[2 * N + 1];
    
    count = 0;
  }
  
  static void dfs(int row) {
    if (row >= N) {
      count++;
      return;
    }
    
    for (int c = 0; c < N; c++) {
      int d1 = row - c + N - 1;
      int d2 = row + c;
      
      if (col[c] || diag1[d1] || diag2[d2]) continue;
      
      col[c] = true;
      diag1[d1] = true;
      diag2[d2] = true;
      
      dfs(row + 1);
      
      col[c] = false;
      diag1[d1] = false;
      diag2[d2] = false;
    }
  }
  
  public static void main(String[] args) throws Exception {
    int T = Integer.parseInt(br.readLine());
    
    for (int t=1; t<=T; t++) {
      init();
      dfs(0);
      sb.append("#").append(t).append(" ").append(count).append("\n");
    }
    
    System.out.print(sb.toString());
  }
}