import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int R, C;
  static char[][] map;
  static boolean[][] visited;

  static int sr, sc;
  static int answer = -1;

  static final int[] dr = {-1,1,0,0};
  static final int[] dc = {0,0,-1,1};

  static class Node {
    // type: 0=물, 1=고슴도치
    int r, c, type, time; 
    Node(int r, int c, int type, int time) {
      this.r = r;
      this.c = c;
      this.type = type;
      this.time = time;
    }
  }

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());

    map = new char[R][C];
    visited = new boolean[R][C];

    for (int r=0; r<R; r++) {
      String line = br.readLine();
      for (int c=0; c<C; c++) {
        map[r][c] = line.charAt(c);
        if (map[r][c] == 'S') {
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

    // 물 먼저
    for (int r=0; r<R; r++) {
      for (int c=0; c<C; c++) {
        if (map[r][c] == '*') {
          queue.add(new Node(r, c, 0, 0));
        }
      }
    }

    // 그 다음 비버
    queue.add(new Node(sr, sc, 1, 0));
    visited[sr][sc] = true;

    while (!queue.isEmpty()) {
      Node cur = queue.poll();

      for (int d=0; d<dr.length; d++) {
        int nr = cur.r + dr[d];
        int nc = cur.c + dc[d];

        if (!isInRange(nr, nc)) continue;
           
        // 물
        if (cur.type == 0) { 
          if (map[nr][nc] == '.' ) {
            map[nr][nc] = '*';
            queue.add(new Node(nr, nc, 0, cur.time+1));
          }
        } 
        // 고슴도치
        else { 
          if (map[nr][nc] == 'D') {
            answer = cur.time + 1;
            return;
          }
          if (map[nr][nc] == '.' && !visited[nr][nc]) {
            visited[nr][nc] = true;
            queue.add(new Node(nr, nc, 1, cur.time+1));
          }
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    init();
    bfs();
    sb.append(answer == -1 ? "KAKTUS" : answer).append("\n");
    System.out.print(sb);
  }
}
