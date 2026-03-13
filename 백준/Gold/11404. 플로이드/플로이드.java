import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  final static int MAX = Integer.MAX_VALUE / 100;
  
  static int N, M;
  static int[][] minDist;
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    M = Integer.parseInt(br.readLine());
    
    minDist = new int[N+1][N+1];
    for (int i=1; i<=N; i++) {
      Arrays.fill(minDist[i], MAX);
      minDist[i][i] = 0;
    }
    
    for (int m=0; m<M; m++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int c = Integer.parseInt(st.nextToken());
      
      minDist[a][b] = Math.min(minDist[a][b], c);
    }
  }
  
  static void solve() {
    floydWarshall();
    appendResult();
  }
  
  static void floydWarshall() {
    for (int k=1; k<=N; k++) {
      for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
          if (i == j) continue;
          minDist[i][j] = Math.min(minDist[i][j], minDist[i][k] + minDist[k][j]);
        }
      }
    }
  }
  
  static void appendResult() {
    for (int r=1; r<=N; r++) {
      for (int c=1; c<=N; c++) {
        int value = minDist[r][c];
        sb.append(value == MAX ? 0 : value).append(" ");
      }
      sb.append("\n");
    }
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.println(sb.toString());
  }
}