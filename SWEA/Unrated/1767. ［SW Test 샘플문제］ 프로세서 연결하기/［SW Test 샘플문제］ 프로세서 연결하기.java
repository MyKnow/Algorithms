import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int T;
  static int N;
  static int[][] map;
  
  static ArrayList<int[]> cores;
  static int maxCore, minWire;
  
  static int[] dr = { -1, 1, 0, 0 };
  static int[] dc = { 0, 0, -1, 1 };
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    map = new int[N][N];
    cores = new ArrayList<>();
    
    for (int r = 0; r < N; r++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int c = 0; c < N; c++) {
        map[r][c] = Integer.parseInt(st.nextToken());
        if (map[r][c] == 1) {
          // 테두리에 붙어있는 코어는 제외
          if (!(r == 0 || r == N - 1 || c == 0 || c == N - 1)) {
            cores.add(new int[]{r, c});
          }
        }
      }
    }
    
    maxCore = 0;
    minWire = Integer.MAX_VALUE;
  }
  
  static void dfs(int idx, int connected, int wire) {
    if (connected + (cores.size() - idx) < maxCore) return;
    
    if (idx == cores.size()) {
      if (connected > maxCore) {
        maxCore = connected;
        minWire = wire;
      } else if (connected == maxCore) {
        minWire = Math.min(minWire, wire);
      }
      return;
    }
    
    int r = cores.get(idx)[0];
    int c = cores.get(idx)[1];
    
    // 1. 전선 이어보기
    for (int d = 0; d < dr.length; d++) {
      int nr = r;
      int nc = c;
      int len = 0;
      boolean canConnect = true;
      
      while (true) {
        nr += dr[d];
        nc += dc[d];
        
        if (!isInRange(nr, nc)) break;
        
        // 코어와 접촉하면 해당 방향 전선 이을 수 없음.
        if (map[nr][nc] != 0) {
          canConnect = false;
          break;
        }
        len++;
      }
      
      if (!canConnect) continue;
      
      nr = r;
      nc = c;
      for (int i = 0; i < len; i++) {
        nr += dr[d];
        nc += dc[d];
        map[nr][nc] = 2;
      }
      
      dfs(idx + 1, connected + 1, wire + len);
      
      nr = r;
      nc = c;
      for (int i = 0; i < len; i++) {
        nr += dr[d];
        nc += dc[d];
        map[nr][nc] = 0;
      }
    }
    
    // 2. 해당 코어 포기하기
    dfs(idx + 1, connected, wire);
  }
  
  static boolean isInRange(int r, int c) {
    return 0 <= r && r < N && 0 <= c && c < N;
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t <= T; t++) {
      init();
      dfs(0, 0, 0);
      sb.append("#").append(t).append(" ").append(minWire).append("\n");
    }
    System.out.print(sb.toString());
  }
}
