import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int answer;
  
  static int R, C;
  static int[][] map;
  
  static int dr[] = { -1, 1, 0, 0 };
  static int dc[] = {  0, 0,-1, 1 };
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
    
    map = new int[R][C];
    for (int r=0; r<R; r++) {
      String line = br.readLine();
      for (int c=0; c<C; c++) {
        map[r][c] = line.charAt(c)-'A';
      }
    }
  }
  
  static void solve() {
    int initMask = masking(0, map[0][0]);
    dfs(0, 0, initMask, 1);
  }
  
  static void dfs(int r, int c, int mask, int depth) {
    answer = Math.max(answer, depth);
    
    for (int d=0; d<dr.length; d++) {
      int nr = r+dr[d];
      int nc = c+dc[d];
      
      if (!isInRange(nr, nc)) continue;
      
      int nv = map[nr][nc];
      if (isAlreadyMasked(mask, nv)) continue;
      
      int nm = masking(mask, nv);
      dfs(nr, nc, nm, depth+1);
    }
  }
  
  static boolean isInRange(int nr, int nc) {
    return 0 <= nr && nr < R && 0 <= nc && nc < C;
  }
  
  static boolean isAlreadyMasked(int mask, int value) {
    return (mask & (1 << value)) != 0;
  }
  
  static int masking(int mask, int value) {
    return mask | (1 << value);
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    sb.append(answer).append("\n");
    System.out.print(sb.toString());
  }
}