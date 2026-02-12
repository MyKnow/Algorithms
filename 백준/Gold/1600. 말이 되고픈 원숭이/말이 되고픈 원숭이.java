import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int K, C, R;
  static int[][] map;
  static boolean[][][] visited;

  static final int[] dr_horse = {-2,-1,1,2,2,1,-1,-2};
  static final int[] dc_horse = {1,2,2,1,-1,-2,-2,-1};
  static final int[] dr_monkey = {-1,1,0,0};
  static final int[] dc_monkey = {0,0,-1,1};

  static int answer;

  static class Node {
    int r, c, k, move;
    Node(int r, int c, int k, int move) {
      this.r = r;
      this.c = c;
      this.k = k;
      this.move = move;
    }
  }

  static void init() throws Exception {
    K = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine());
    C = Integer.parseInt(st.nextToken());
    R = Integer.parseInt(st.nextToken());

    map = new int[R][C];
    visited = new boolean[R][C][K+1];

    for (int r=0; r<R; r++) {
      st = new StringTokenizer(br.readLine());
      for (int c=0; c<C; c++) {
        map[r][c] = Integer.parseInt(st.nextToken());
      }
    }

    answer = -1;
  }

  static boolean isInRange(int nr, int nc) {
    return (0 <= nr && nr < R && 0 <= nc && nc < C);
  }

  static void bfs() {
    ArrayDeque<Node> queue = new ArrayDeque<>();
    queue.add(new Node(0, 0, K, 0));
    visited[0][0][K] = true;

    while (!queue.isEmpty()) {
      Node cur = queue.poll();

      if (cur.r == R-1 && cur.c == C-1) {
        answer = cur.move;
        return;
      }

      // 일반 이동
      for (int d=0; d<dr_monkey.length; d++) {
        int nr = cur.r + dr_monkey[d];
        int nc = cur.c + dc_monkey[d];

        if (!isInRange(nr, nc)) continue;
        if (map[nr][nc] == 1) continue;
        if (!visited[nr][nc][cur.k]) {
          visited[nr][nc][cur.k] = true;
          queue.add(new Node(nr, nc, cur.k, cur.move+1));
        }
      }

      // 말 이동
      if (cur.k > 0) {
        for (int d=0; d<dr_horse.length; d++) {
          int nr = cur.r + dr_horse[d];
          int nc = cur.c + dc_horse[d];

          if (!isInRange(nr, nc)) continue;
          if (map[nr][nc] == 1) continue;
          if (!visited[nr][nc][cur.k-1]) {
            visited[nr][nc][cur.k-1] = true;
            queue.add(new Node(nr, nc, cur.k-1, cur.move+1));
          }
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    init();
    bfs();
    sb.append(answer).append("\n");
    System.out.print(sb);
  }
}
