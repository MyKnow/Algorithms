import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  static int N, M;
  static int[][] map;
  static int[][] temp;

  static int[] emptyR = new int[64];
  static int[] emptyC = new int[64];
  static int emptySize;

  static int maxSafe;

  static final int[] dr = {-1, 1, 0, 0};
  static final int[] dc = {0, 0, -1, 1};

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    map = new int[N][M];
    temp = new int[N][M];
    emptySize = 0;
    maxSafe = 0;

    for (int r = 0; r < N; r++) {
      st = new StringTokenizer(br.readLine());
      for (int c = 0; c < M; c++) {
        map[r][c] = Integer.parseInt(st.nextToken());
        if (map[r][c] == 0) {
          emptyR[emptySize] = r;
          emptyC[emptySize] = c;
          emptySize++;
        }
      }
    }
  }

  static void buildWalls(int start, int depth) {
    if (depth == 3) {
      spreadVirus();
      return;
    }

    for (int i = start; i < emptySize; i++) {
      int r = emptyR[i];
      int c = emptyC[i];

      map[r][c] = 1;
      buildWalls(i + 1, depth + 1);
      map[r][c] = 0;
    }
  }

  static void spreadVirus() {
    copyMap();

    ArrayDeque<int[]> queue = new ArrayDeque<>();

    for (int r = 0; r < N; r++) {
      for (int c = 0; c < M; c++) {
        if (temp[r][c] == 2) {
          queue.add(new int[] {r, c});
        }
      }
    }

    while (!queue.isEmpty()) {
      int[] cur = queue.poll();
      int r = cur[0];
      int c = cur[1];

      for (int d = 0; d < 4; d++) {
        int nr = r + dr[d];
        int nc = c + dc[d];

        if (nr < 0 || nc < 0 || nr >= N || nc >= M) continue;
        if (temp[nr][nc] != 0) continue;

        temp[nr][nc] = 2;
        queue.add(new int[] {nr, nc});
      }
    }

    countSafe();
  }

  static void copyMap() {
    for (int r = 0; r < N; r++) {
      for (int c = 0; c < M; c++) {
        temp[r][c] = map[r][c];
      }
    }
  }

  static void countSafe() {
    int count = 0;

    for (int r = 0; r < N; r++) {
      for (int c = 0; c < M; c++) {
        if (temp[r][c] == 0) count++;
      }
    }

    if (count > maxSafe) maxSafe = count;
  }

  public static void main(String[] args) throws Exception {
    init();
    buildWalls(0, 0);
    System.out.print(maxSafe);
  }
}
