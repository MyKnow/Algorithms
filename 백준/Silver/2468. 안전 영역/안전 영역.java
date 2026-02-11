import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int answer;
  
  static int N;
  static int[][] gangnam;
  static int maxHeight;
  static int minHeight;
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    
    minHeight = Integer.MAX_VALUE;
    maxHeight = 0;
    gangnam = new int[N][N];
    for (int r=0; r<N; r++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int c=0; c<N; c++) {
        int currentHeight = Integer.parseInt(st.nextToken());
        minHeight = Math.min(minHeight, currentHeight);
        maxHeight = Math.max(maxHeight, currentHeight);
        gangnam[r][c] = currentHeight;
      }
    }
    
    answer = 1;
  }
  
  static void solve() {
    for (int w=minHeight; w<maxHeight; w++) {
      int[][] backup = new int[N][N];
      for (int r=0; r<N; r++) {
        for (int c=0; c<N; c++) {
          backup[r][c] = gangnam[r][c];
        }
      }
      
      floodGangnam(w);
      int result = countSafeArea();
      answer = Math.max(answer, result);
      
      for (int r=0; r<N; r++) {
        for (int c=0; c<N; c++) {
          gangnam[r][c] = backup[r][c];
        }
      }
    }
  }
  
  static void floodGangnam(int waterLevel) {
    for (int r=0; r<N; r++) {
      for (int c=0; c<N; c++) {
        int currentLevel = gangnam[r][c];
        if (currentLevel <= waterLevel) {
          gangnam[r][c] = 0;
        }
      }
    }
  }
  
  static int countSafeArea() {
    int count = 0;
    for (int r=0; r<N; r++) {
      for (int c=0; c<N; c++) {
        if (gangnam[r][c] != 0) {
          dfs(r, c);
          count++;
        }
      }
    }
    return count;
  }
  
  static int[] dr = { -1, 1, 0, 0 };
  static int[] dc = {  0, 0,-1, 1 };
  static void dfs(int r, int c) {
    ArrayDeque<int[]> queue = new ArrayDeque<>();
    queue.addLast( new int[] { r, c } );
    gangnam[r][c] = 0;
    
    while(!queue.isEmpty()) {
      int[] curCoords = queue.pollLast();
      int cr = curCoords[0];
      int cc = curCoords[1];
      
      for (int d=0; d<dr.length; d++) {
        int nr = cr + dr[d], nc = cc + dc[d];
        
        if (!isInRange(nr, nc) || gangnam[nr][nc] == 0) continue;
        
        gangnam[nr][nc] = 0;
        queue.addLast ( new int[] { nr, nc } );
      }
    }
  }
  static boolean isInRange(int nr, int nc) {
    return (0 <= nr && nr < N && 0 <= nc && nc < N);
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    sb.append(answer).append("\n");
    System.out.print(sb.toString());
  }
}