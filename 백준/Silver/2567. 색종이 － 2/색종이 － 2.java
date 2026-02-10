import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static final int SIZE = 101;
  static int[][] map = new int[SIZE][SIZE];

  static int[] dr = { -1, 1, 0, 0 };
  static int[] dc = { 0, 0, -1, 1 };

  static boolean isOutOfMap(int r, int c) {
    return r < 0 || r >= SIZE || c < 0 || c >= SIZE;
  }

  static boolean isBoundary(int r, int c, int d) {
    int nr = r + dr[d];
    int nc = c + dc[d];

    if (isOutOfMap(nr, nc)) return true;
    if (map[nr][nc] == 0) return true;

    return false;
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    for (int i = 0; i < N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());

      for (int r = y; r < y + 10; r++) {
        for (int c = x; c < x + 10; c++) {
          map[r][c] = 1;
        }
      }
    }

    int perimeter = 0;

    for (int r = 0; r < SIZE; r++) {
      for (int c = 0; c < SIZE; c++) {
        if (map[r][c] == 1) {
          for (int d = 0; d < 4; d++) {
            if (isBoundary(r, c, d)) {
              perimeter++;
            }
          }
        }
      }
    }

    System.out.println(perimeter);
  }
}
