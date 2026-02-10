import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  static int N, M;
  static int[][] map;
  static int[][] cctv;
  static int cctvCnt;
  static int answer;

  static int[] dr = {-1, 0, 1, 0};
  static int[] dc = {0, 1, 0, -1};

  static int[][][] dir = {
    {},
    {{0},{1},{2},{3}},
    {{0,2},{1,3}},
    {{0,1},{1,2},{2,3},{3,0}},
    {{0,1,2},{1,2,3},{2,3,0},{3,0,1}},
    {{0,1,2,3}}
  };

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    map = new int[N][M];
    cctv = new int[8][3];
    cctvCnt = 0;

    for (int r = 0; r < N; r++) {
      st = new StringTokenizer(br.readLine());
      for (int c = 0; c < M; c++) {
        map[r][c] = Integer.parseInt(st.nextToken());
        if (1 <= map[r][c] && map[r][c] <= 5) {
          cctv[cctvCnt][0] = r;
          cctv[cctvCnt][1] = c;
          cctv[cctvCnt][2] = map[r][c];
          cctvCnt++;
        }
      }
    }

    answer = Integer.MAX_VALUE;
  }

  static void dfs(int idx) {
    if (idx == cctvCnt) {
      answer = Math.min(answer, countBlind());
      return;
    }

    int r = cctv[idx][0];
    int c = cctv[idx][1];
    int type = cctv[idx][2];

    for (int[] dset : dir[type]) {
      int[][] backup = copyMap();
      for (int d : dset) watch(r, c, d);
      dfs(idx + 1);
      map = backup;
    }
  }

  static void watch(int r, int c, int d) {
    int nr = r;
    int nc = c;

    while (true) {
      nr += dr[d];
      nc += dc[d];

      if (!isInRange(nr, nc) || map[nr][nc] == 6) break;
      if (map[nr][nc] == 0) map[nr][nc] = -1;
    }
  }

  static int countBlind() {
    int cnt = 0;
    for (int r = 0; r < N; r++) {
      for (int c = 0; c < M; c++) {
        if (map[r][c] == 0) cnt++;
      }
    }
    return cnt;
  }

  static boolean isInRange(int r, int c) {
    return (0 <= r && r < N && 0 <= c && c < M);
  }

  static int[][] copyMap() {
    int[][] tmp = new int[N][M];
    for (int i = 0; i < N; i++) {
      System.arraycopy(map[i], 0, tmp[i], 0, M);
    }
    return tmp;
  }

  public static void main(String[] args) throws Exception {
    init();
    dfs(0);
    System.out.print(answer);
  }
}
