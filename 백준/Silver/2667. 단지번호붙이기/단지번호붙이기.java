import java.io.*;
import java.util.*;

public class Main {
  static int N;
  static int[][] map;
  static int[] countMap;
  static int count;
  
  final static int[] dr = { -1, 1, 0, 0 };
  final static int[] dc = {  0, 0,-1, 1 };
  static void dfs(int r, int c) {
    for (int d=0; d<dr.length; d++) {
      int nr = r+dr[d], nc = c+dc[d];
      if (isInbound(nr, nc) && map[nr][nc] == -1) {
        countMap[count]++;
        map[nr][nc] = count;
        dfs(nr, nc);
      }
    }
  }
  
  static boolean isInbound(int nr, int nc) {
    return (0 <= nr && nr < N && 0 <= nc && nc < N);
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    map = new int[N][N];

    StringTokenizer st;
    for (int r=0; r<N; r++) {
      char[] line = br.readLine().toCharArray();
      for (int c=0; c<N; c++) {
        map[r][c] = (line[c]-'0') * -1;
      }
    }
    
    count = 0;
    countMap = new int[N*N+1];
    for (int r=0; r<N; r++) {
      for (int c=0; c<N; c++) {
        if (map[r][c] == -1) {
          count++;
          map[r][c] = count;
          countMap[count] = 1;
          dfs(r, c);
        }
      }
    }
    
    StringBuilder sb = new StringBuilder();
    Arrays.sort(countMap, 1, count+1);
    sb.append(count).append("\n");
    for (int i=1; i<=count; i++) {
      sb.append(countMap[i]).append("\n");
    }
    System.out.print(sb.toString());
  }
}