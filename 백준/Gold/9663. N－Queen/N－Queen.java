import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  
  static int N;
  static int count;
  
  static boolean[] col;
  static boolean[] lt2rd;
  static boolean[] ld2rt;
  
  static void dfs(int row) {
    if (row == N) {
      count++;
      return;
    }
    
    for (int c = 0; c < N; c++) {
      int d1 = (N - 1) + c - row;
      int d2 = c + row;
      
      if (col[c] || lt2rd[d1] || ld2rt[d2]) continue;
      
      col[c] = true;
      lt2rd[d1] = true;
      ld2rt[d2] = true;
      
      dfs(row + 1);
      
      col[c] = false;
      lt2rd[d1] = false;
      ld2rt[d2] = false;
    }
  }
  
  public static void main(String[] args) throws Exception {
    N = Integer.parseInt(br.readLine());
    
    col = new boolean[N];
    lt2rd = new boolean[2 * N - 1];
    ld2rt = new boolean[2 * N - 1];
    
    count = 0;
    dfs(0);
    
    System.out.println(count);
  }
}