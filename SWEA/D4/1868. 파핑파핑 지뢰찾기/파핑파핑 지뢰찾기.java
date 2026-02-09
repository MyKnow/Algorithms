import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T;
  
  static int N;
  static int answer;
  static char[][] map;
  static boolean[][] visited;
  
  static final int[] dr = {-1,-1,-1,0,0,1,1,1};
  static final int[] dc = {-1,0,1,-1,1,-1,0,1};
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    map = new char[N][N];
    visited = new boolean[N][N];
    answer = 0;
    
    for (int i = 0; i < N; i++) {
      String line = br.readLine();
      for (int j = 0; j < N; j++) {
        map[i][j] = line.charAt(j);
      }
    }
  }
  
  static void solveTestCase() throws Exception {
    // 1. 주변 지뢰가 0인 칸들부터 클릭
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (map[i][j] == '.' && !visited[i][j] && countMine(i, j) == 0) {
          bfs(i, j);
          answer++;
        }
      }
    }
    
    // 2. 아직 방문되지 않은 나머지 숫자 칸
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (map[i][j] == '.' && !visited[i][j]) {
          answer++;
        }
      }
    }
  }
  
  static void bfs(int sr, int sc) {
    Queue<int[]> q = new ArrayDeque<>();
    visited[sr][sc] = true;
    q.offer(new int[]{sr, sc});
    
    while (!q.isEmpty()) {
      int[] cur = q.poll();
      int cr = cur[0];
      int cc = cur[1];
      
      if (countMine(cr, cc) != 0) continue;
      
      for (int d = 0; d < dr.length; d++) {
        int nr = cr + dr[d];
        int nc = cc + dc[d];
        
        if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
        if (visited[nr][nc]) continue;
        if (map[nr][nc] == '*') continue;
        
        visited[nr][nc] = true;
        q.offer(new int[]{nr, nc});
      }
    }
  }
  
  static int countMine(int r, int c) {
    int cnt = 0;
    
    for (int d = 0; d < dr.length; d++) {
      int nr = r + dr[d];
      int nc = c + dc[d];
      
      if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
      if (map[nr][nc] == '*') cnt++;
    }
    return cnt;
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t <= T; t++) {
      init();
      solveTestCase();
      sb.append("#").append(t).append(" ").append(answer).append("\n");
    }
    System.out.print(sb.toString());
  }
}
