import java.util.*;
import java.io.*;

public class Main {
  static int N;
  static int M;
  static int[][] pSum;
  
  static int getRSum(int startR, int startC, int endR, int endC) {
    return pSum[endR][endC] - (pSum[endR][startC-1] + pSum[startR-1][endC] - pSum[startR-1][startC-1]);
  }
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    pSum = new int[N+1][N+1];
    for (int r=1; r<=N; r++) {
      st = new StringTokenizer(br.readLine());
      for (int c=1; c<=N; c++) {
        int value = Integer.parseInt(st.nextToken());
        pSum[r][c] = value + pSum[r-1][c] + pSum[r][c-1] - pSum[r-1][c-1];
      }
    }
    
    StringBuilder sb = new StringBuilder();
    for (int i=0; i<M; i++) {
      st = new StringTokenizer(br.readLine());
      int sR = Integer.parseInt(st.nextToken());
      int sC = Integer.parseInt(st.nextToken());
      int eR = Integer.parseInt(st.nextToken());
      int eC = Integer.parseInt(st.nextToken());
      sb.append(getRSum(sR, sC, eR, eC)).append("\n");
    }
    
    System.out.print(sb.toString());
  }
}
