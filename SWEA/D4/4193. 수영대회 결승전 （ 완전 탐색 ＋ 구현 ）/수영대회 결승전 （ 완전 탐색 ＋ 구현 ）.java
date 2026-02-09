import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T, answer;
  static int N;
  static int[][] pool;
  static boolean isVisited[][][];
  static int[] srcCoords = new int[2];
  static int[] dstCoords = new int[2];
  
  static int[] dr = { -1, 1, 0, 0 };
  static int[] dc = {  0, 0,-1, 1 };
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    StringTokenizer st;
    
    pool = new int[N][N];
    isVisited = new boolean[N][N][3];
    for (int r=0; r<N; r++) {
      st = new StringTokenizer(br.readLine());
      for (int c=0; c<N; c++) {
        pool[r][c] = Integer.parseInt(st.nextToken());
      }
    }
    
    st = new StringTokenizer(br.readLine());
    srcCoords[0] = Integer.parseInt(st.nextToken());
    srcCoords[1] = Integer.parseInt(st.nextToken());
    
    st = new StringTokenizer(br.readLine());
    dstCoords[0] = Integer.parseInt(st.nextToken());
    dstCoords[1] = Integer.parseInt(st.nextToken());
  }
  
  static int bfs() throws Exception {
    ArrayDeque<int[]> queue = new ArrayDeque<>();
    int t = 0;
    queue.addFirst( new int[] { srcCoords[0], srcCoords[1], t } );
    isVisited[srcCoords[0]][srcCoords[1]][t] = true;
    
    while (!queue.isEmpty()) {
      int[] crtCoords = queue.pollLast();
      int cr = crtCoords[0];
      int cc = crtCoords[1];
      int ct = crtCoords[2];
      
      if (cr == dstCoords[0] && cc == dstCoords[1]) return ct;
      
      for (int d=0; d<dr.length; d++) {
        int nr = cr + dr[d];
        int nc = cc + dc[d];
        int nt = ct + 1;
        
        // 범위 밖 또는 장애물 무시
        if (!isInRange(nr, nc) || pool[nr][nc] == 1) continue;
        
        // 소용돌이 기다리기
        if (pool[nr][nc] == 2 && (nt%3 != 0)) {
          isVisited[cr][cc][nt % 3] = true;
          queue.addFirst( new int[] { cr, cc, nt } );
          continue;
        }
        
        // 일반 상황
        if (!isVisited[nr][nc][nt % 3]) {
          isVisited[nr][nc][nt % 3] = true;
          queue.addFirst( new int[] { nr, nc, nt } );
        }
      }
    }
    
    return -1;
  }
  
  static boolean isInRange(int nr, int nc) {
    return (0 <= nr && nr < N && 0 <= nc && nc < N);
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t=1; t<=T; t++) {
      init();
      int answer = bfs();
      sb.append("#").append(t).append(" ").append(answer).append("\n");
    }
    System.out.print(sb.toString());
  }
}