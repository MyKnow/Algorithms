import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int R, C;
  static int[][] map;
  static boolean[][][] visited;

  static final int[] dr = {-1,1,0,0};
  static final int[] dc = {0,0,-1,1};

  static int answer;

  static class Node {
    int r, c, broke, move;
    Node(int r, int c, int broke, int move) {
      this.r = r;
      this.c = c;
      // 0: 아직 벽 안부숨, 1: 이미 벽 부숨
      this.broke = broke; 
      this.move = move;
    }
  }

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());

    map = new int[R][C];
    visited = new boolean[R][C][2];

    for (int r=0; r<R; r++) {
      String line = br.readLine();
      for (int c=0; c<C; c++) {
        map[r][c] = line.charAt(c) - '0';
      }
    }
    
    answer = -1;
  }

  static boolean isInRange(int nr, int nc) {
    return 0 <= nr && nr < R && 0 <= nc && nc < C;
  }

  static void bfs() {
    ArrayDeque<Node> queue = new ArrayDeque<>();
    queue.add(new Node(0, 0, 0, 1));
    visited[0][0][0] = true;

    while (!queue.isEmpty()) {
      Node cur = queue.poll();

      if (cur.r == R-1 && cur.c == C-1) {
        answer = cur.move;
        return;
      }

      for (int d=0; d<dr.length; d++) {
        int nr = cur.r + dr[d];
        int nc = cur.c + dc[d];

        if (!isInRange(nr,nc)) continue;

        // 방문한 적 없는 길만 진행 
        if (map[nr][nc] == 0 && !visited[nr][nc][cur.broke]) {
          visited[nr][nc][cur.broke] = true;
          queue.add(new Node(nr, nc, cur.broke, cur.move+1));
        } 
        // 이미 부숴본 벽이 아니라면 진행
        else if (map[nr][nc] == 1 && cur.broke == 0 && !visited[nr][nc][1]) {
          visited[nr][nc][1] = true;
          queue.add(new Node(nr, nc, 1, cur.move+1));
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
