import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static final int R = 12;
  static final int C = 6;

  static char[][] map;
  static boolean[][] visited;

  static int[] dr = {-1,1,0,0};
  static int[] dc = {0,0,-1,1};

  static int chainCount = 0;

  static void init() throws Exception {
    map = new char[R][C];
    for (int r = 0; r < R; r++) {
      String line = br.readLine();
      for (int c = 0; c < C; c++) {
        map[r][c] = line.charAt(c);
      }
    }
  }

  static boolean dfs(int r, int c, char color, boolean mark) {
    visited[r][c] = true;
    boolean exploded = false;
    int count = 1;
    int top = 0;
    int[][] stack = new int[R*C][2];
    stack[top++] = new int[]{ r, c };

    for (int i = 0; i < top; i++) {
      int cr = stack[i][0];
      int cc = stack[i][1];

      for (int d = 0; d < dr.length; d++) {
        int nr = cr + dr[d];
        int nc = cc + dc[d];

        if (!isInRange(nr,nc)) continue;
        if (visited[nr][nc] || map[nr][nc] != color) continue;

        visited[nr][nc] = true;
        stack[top++] = new int[]{ nr, nc };
        count++;
      }
    }

    if (count >= 4) {
      exploded = true;
      if (mark) {
        for (int i = 0; i < top; i++) {
          int er = stack[i][0];
          int ec = stack[i][1];
          map[er][ec] = '.';
        }
      }
    }

    return exploded;
  }

  // 물귀신
  static void applyGravity() {
    for (int c = 0; c < C; c++) {
      for (int r = R-1; r >=0; r--) {
        if (map[r][c] == '.') {
          int nr = r-1;
          while (nr >=0 && map[nr][c] == '.') nr--;
          if (nr >=0) {
            map[r][c] = map[nr][c];
            map[nr][c] = '.';
          }
        }
      }
    }
  }

  static boolean process() {
    visited = new boolean[R][C];
    boolean anyExploded = false;

    for (int r=0; r<R; r++) {
      for (int c=0; c<C; c++) {
        if (!visited[r][c] && map[r][c] != '.') {
          boolean exploded = dfs(r,c,map[r][c],true);
          if (exploded) anyExploded = true;
        }
      }
    }

    if (anyExploded) {
      applyGravity();
      chainCount++;
    }

    return anyExploded;
  }

  static boolean isInRange(int r, int c) {
    return 0 <= r && r < R && 0 <= c && c < C;
  }

  public static void main(String[] args) throws Exception {
    init();
    while (process()) { }
    sb.append(chainCount).append("\n");
    System.out.print(sb);
  }
}
