import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int N;
  static int[][] map;
  static int[][] minCost;

  static final int[] dr = {-1,1,0,0};
  static final int[] dc = {0,0,-1,1};

  static class Node {
    int r, c, total;
    Node(int r, int c, int total) {
      this.r = r;
      this.c = c;
      this.total = total;
    }
  }

  static void init() throws Exception {
    map = new int[N][N];
    minCost = new int[N][N];

    for (int r=0; r<N; r++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int c=0; c<N; c++) {
        map[r][c] = Integer.parseInt(st.nextToken());
        minCost[r][c] = Integer.MAX_VALUE;
      }
    }
  }

  static boolean isInRange(int nr, int nc) {
    return 0 <= nr && nr < N && 0 <= nc && nc < N;
  }

  static void bfs() {
    ArrayDeque<Node> queue = new ArrayDeque<>();
    queue.add(new Node(0,0,map[0][0]));
    minCost[0][0] = map[0][0];

    while (!queue.isEmpty()) {
      Node cur = queue.poll();

      for (int d=0; d<dr.length; d++) {
        int nr = cur.r + dr[d];
        int nc = cur.c + dc[d];

        if (!isInRange(nr,nc)) continue;

        int nextCost = cur.total + map[nr][nc];
        if (nextCost < minCost[nr][nc]) {
          minCost[nr][nc] = nextCost;
          queue.add(new Node(nr,nc,nextCost));
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    int testCase = 1;
    while (true) {
      N = Integer.parseInt(br.readLine());
      if (N == 0) break;

      init();
      bfs();
      sb.append("Problem ").append(testCase++).append(": ").append(minCost[N-1][N-1]).append("\n");
    }
    System.out.print(sb);
  }
}
