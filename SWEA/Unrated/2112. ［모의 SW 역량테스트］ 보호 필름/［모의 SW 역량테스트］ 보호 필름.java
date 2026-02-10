import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int T;
  static int D, W, K;
  static int[][] film;
  static int answer;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    D = Integer.parseInt(st.nextToken());
    W = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());
    
    film = new int[D][W];
    for (int i = 0; i < D; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < W; j++) {
        film[i][j] = Integer.parseInt(st.nextToken());
      }
    }
      
    // 최악: K개 행에 약품 주입
    answer = K; 
  }
  
  static void dfs(int row, int used) {
    if (used >= answer) return;
    
    if (row == D) {
      if (check()) {
        answer = used;
      }
      return;
    }
    
    // 1. 주입 안 함
    dfs(row + 1, used);
    
    int[] backup = film[row].clone();
    
    // 2. A 주입 (0)
    fillRow(row, 0);
    dfs(row + 1, used + 1);
    
    // 3. B 주입 (1)
    fillRow(row, 1);
    dfs(row + 1, used + 1);
    
    // 복구
    film[row] = backup;
  }
  
  static void fillRow(int row, int val) {
    for (int c = 0; c < W; c++) {
      film[row][c] = val;
    }
  }
  
  static boolean check() {
    for (int c = 0; c < W; c++) {
      int cnt = 1;
      int prev = film[0][c];
      boolean pass = false;
      
      for (int r = 1; r < D; r++) {
        if (film[r][c] == prev) {
          cnt++;
        } else {
          prev = film[r][c];
          cnt = 1;
        }
        
        if (cnt >= K) {
          pass = true;
          break;
        }
      }
      
      if (!pass) return false;
    }
    return true;
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
