import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int R, C;
  static char[][] map;
  static boolean[][][] visited;
  static int sr, sc;

  static final int[] dr = {-1,1,0,0};
  static final int[] dc = {0,0,-1,1};

  static int answer;

  static class Node {
    int r, c, keys, move;
    Node(int r, int c, int keys, int move) {
      this.r = r;
      this.c = c;
      this.keys = keys;
      this.move = move;
    }
  }

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());

    map = new char[R][C];
    visited = new boolean[R][C][1<<6];
    sr = sc = -1;

    for (int r=0; r<R; r++) {
      String line = br.readLine();
      for (int c=0; c<C; c++) {
        map[r][c] = line.charAt(c);
        if (map[r][c] == '0') {
          sr = r;
          sc = c;
        }
      }
    }

    answer = -1;
  }

  static boolean isInRange(int r, int c) {
    return 0 <= r && r < R && 0 <= c && c < C;
  }

  static void bfs() {
    ArrayDeque<Node> queue = new ArrayDeque<>();
    queue.add(new Node(sr, sc, 0, 0));
    visited[sr][sc][0] = true;

    while (!queue.isEmpty()) {
      Node cur = queue.poll();

      if (map[cur.r][cur.c] == '1') {
        answer = cur.move;
        return;
      }

      for (int d=0; d<dr.length; d++) {
        int nr = cur.r + dr[d];
        int nc = cur.c + dc[d];
        int keys = cur.keys;

        if (!isInRange(nr,nc)) continue;
        char cell = map[nr][nc];
        if (cell == '#') continue;

        // 문: 열쇠 없으면 이동 불가
        if ('A' <= cell && cell <= 'F') {
          if ((keys & (1<<(cell-'A'))) == 0) continue;
        }

        // 열쇠 획득
        if ('a' <= cell && cell <= 'f') {
          keys |= (1<<(cell-'a'));
        }

        if (!visited[nr][nc][keys]) {
          visited[nr][nc][keys] = true;
          queue.add(new Node(nr, nc, keys, cur.move+1));
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    init();
    bfs();
    sb.append(answer).append("\n");
    System.out.print(sb.toString());
  }
}
