import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashSet;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int maxDepth;
  
  static int R, C;
  static int[][] board;
  static HashSet<Integer>[][] visitedMask;
  
  static int dr[] = { -1, 1, 0, 0 };
  static int dc[] = {  0, 0,-1, 1 };
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
    
    board = new int[R][C];
    visitedMask = (HashSet<Integer>[][]) new HashSet[R][C];
    for (int r=0; r<R; r++) {
      String line = br.readLine();
      for (int c=0; c<C; c++) {
        board[r][c] = line.charAt(c)-'A';
        visitedMask[r][c] = new HashSet<Integer>();
      }
    }
  }
  
  static void solve() {
    int mask = setBit(0, board[0][0]);
    visitedMask[0][0].add(mask);
    dfs(0, 0, mask, 1);
  }
  
  static void dfs(int r, int c, int mask, int depth) {
    maxDepth = Math.max(maxDepth, depth);
    if (maxDepth == 'Z'-'A'+1) return;
    
    for (int d=0; d<dr.length; d++) {
      int nr = r+dr[d];
      int nc = c+dc[d];
      
      if (!isInRange(nr, nc)) continue;
      
      int nv = board[nr][nc];
      if (isAlreadyMasked(mask, nv)) continue;
      
      int nm = setBit(mask, nv);
      if (isAlreadyVisited(nr, nc, nm)) continue;
      
      visitedMask[nr][nc].add(nm);
      dfs(nr, nc, nm, depth+1);
    }
  }
  
  static boolean isInRange(int nr, int nc) {
    return 0 <= nr && nr < R && 0 <= nc && nc < C;
  }
  
  static boolean isAlreadyMasked(int mask, int value) {
    return (mask & (1 << value)) != 0;
  }
  
  static int setBit(int mask, int value) {
    return mask | (1 << value);
  }
  
  static boolean isAlreadyVisited(int nr, int nc, int mask) {
    return visitedMask[nr][nc].contains(mask);
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    sb.append(maxDepth).append("\n");
    System.out.print(sb.toString());
  }
}