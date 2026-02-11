import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int answer;
  
  static int R, C;
  static int[][] map;
  static boolean[][] isVisited;
  
  static boolean isInRange(int nr, int nc) {
    return (0 <= nr && nr < R && 0 <= nc && nc < C);
  }
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
    
    map = new int[R][C];
    isVisited = new boolean[R][C];
    for (int r=0; r<R; r++) {
      st = new StringTokenizer(br.readLine());
      for (int c=0; c<C; c++) {
        map[r][c] = Integer.parseInt(st.nextToken());
      }
    }
    
    answer = 0;
  }
  
  static void solution() {
    for (int r=0; r<R; r++) {
      for (int c=0; c<C; c++) {
        // 1. 4가지 도형 시도 및 최대값 업데이트
        isVisited[r][c] = true;
        dfs(r, c, 1, map[r][c]);
        isVisited[r][c] = false;
        
        // 2. T자 모양 시도 및 최대값 업데이트
        tryShapeOfT(r, c);
      }
    }
  }
  
  static int[] dr = { -1, 1, 0, 0 };
  static int[] dc = {  0, 0,-1, 1 };
  static void dfs(int r, int c, int length, int sum) {
    if (length == 4) {
      answer = Math.max(answer, sum);
      return;
    }
    
    for (int d=0; d<dr.length; d++) {
      int nr = r + dr[d];
      int nc = c + dc[d];
      
      if (!isInRange(nr, nc) || isVisited[nr][nc]) continue;
      
      isVisited[nr][nc] = true;
      dfs(nr, nc, length+1, sum+map[nr][nc]);
      isVisited[nr][nc] = false;
    }
  }
  
  static void tryShapeOfT(int r, int c) {
    for (int skip=0; skip<4; skip++) {
      int sum = map[r][c];
      boolean valid = true;

      for (int d=0; d<4; d++) {
        if (d == skip) continue;

        int nr = r + dr[d];
        int nc = c + dc[d];

        if (!isInRange(nr, nc)) {
          valid = false;
          break;
        }
        sum += map[nr][nc];
      }

      if (valid) {
        answer = Math.max(answer, sum);
      }
    }
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solution();
    sb.append(answer).append("\n");
    System.out.print(sb.toString());
  }
}
