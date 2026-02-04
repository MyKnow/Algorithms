import java.util.*;
import java.io.*;

public class Main {
  static boolean[][] paper = new boolean[100][100];
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    
    for (int i=0; i<N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int ul = Integer.parseInt(st.nextToken());
      int dr = Integer.parseInt(st.nextToken());
      
      for (int r=ul; r<ul+10; r++) {
        for (int c=dr; c<dr+10; c++) {
          paper[r][c] = true;
        }
      }
    }
    
    int sum = 0;
    for (int r=0; r<100; r++) {
      for (int c=0; c<100; c++) {
        sum += (paper[r][c] ? 1 : 0);
      }
    }
    System.out.println(sum);
  }
}