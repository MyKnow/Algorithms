import java.util.*;
import java.io.*;

public class Main {
  static int C, R;
  static int[][] map;
  static int result;
  
  static int[] dr = { -1, -1, 0, 1, 1, 1, 0, -1 };
  static int[] dc = {  0,  1, 1, 1, 0,-1,-1, -1 };
  static void removeIsland(int r, int c) {
    if (map[r][c] != 1) return;
    
    map[r][c] = 0;
    for (int d=0; d<dr.length; d++) {
      int nr = r+dr[d], nc = c+dc[d];
      if (isInbound(nr, nc)) removeIsland(nr, nc);
    }
  }
  
  static boolean isInbound(int nr, int nc) {
    return (0 <= nr && nr < R && 0 <= nc && nc < C);
  }
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    
    while(true) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      C = Integer.parseInt(st.nextToken());
      R = Integer.parseInt(st.nextToken());
      if (C == R && R == 0) break;
      
      map = new int[R][C];
      for (int r=0; r<R; r++) {
        st = new StringTokenizer(br.readLine());
        for (int c=0; c<C; c++) {
          map[r][c] = Integer.parseInt(st.nextToken());
        }
      }
      
      result = 0;
      for (int r=0; r<R; r++) {
        for (int c=0; c<C; c++) {
          if (map[r][c] == 1) {
            result += 1;
            removeIsland(r, c);
          }
        }
      }
      sb.append(result).append("\n");
    }
    
    System.out.print(sb.toString());
  }
}