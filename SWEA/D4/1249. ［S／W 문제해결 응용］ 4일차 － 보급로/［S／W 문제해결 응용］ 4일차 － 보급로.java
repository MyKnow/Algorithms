import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.PriorityQueue;

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T, minTime;
  
  static int N;
  static int[][] map;
  static int[][] visited;
  
  static int[] dr = { 1, 0, 0,-1 };
  static int[] dc = { 0, 1,-1, 0 };
  
  static class Road {
    int r, c, sTime;
    
    Road (int r, int c, int sTime) {
      this.r = r;
      this.c = c;
      this.sTime = sTime;
    }
  }
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    map = new int[N][N];
    visited = new int[N][N];
    
    for (int r=0; r<N; r++) {
      String line = br.readLine();
      for (int c=0; c<N; c++) {
        map[r][c] = line.charAt(c) - '0';
        visited[r][c] = Integer.MAX_VALUE;
      }
    }
    minTime = Integer.MAX_VALUE;
  }
  
  static void dijkstra() {
    PriorityQueue<Road> pq = new PriorityQueue<>((a, b) -> a.sTime - b.sTime);
    pq.offer( new Road(0, 0, 0) );
    visited[0][0] = 0;
    
    while (!pq.isEmpty()) {
      Road currentRoad = pq.poll();
      
      if (currentRoad.r == N-1 && currentRoad.c == N-1) {
        minTime = currentRoad.sTime;
        return;
      }
      
      if (minTime < currentRoad.sTime) continue;
      
      for (int d=0; d<dr.length; d++) {
        int nr = currentRoad.r + dr[d];
        int nc = currentRoad.c + dc[d];
        
        if (!isInRange(nr, nc)) continue;
        
        int ns = currentRoad.sTime + map[nr][nc];
        int ps = visited[nr][nc];
        if (ns >= ps) continue;
        
        visited[nr][nc] = ns;
        pq.offer ( new Road(nr, nc, ns) );
      }
    }
  }
  
  static boolean isInRange(int nr, int nc) {
    return 0 <= nr && nr < N && 0 <= nc && nc < N;
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    for (int t=1; t<=T; t++) {
      init();
      dijkstra();
      sb.append("#").append(t).append(" ").append(minTime).append("\n");
    }
    System.out.print(sb.toString());
  }
}