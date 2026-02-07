import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int TC;
  static int N, M;
  static String answer;
  
  static void solveTestCase() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    
    int mask = (1 << N) - 1;
    answer = ((M & mask) == mask) ? "ON" : "OFF";
  }
  
  public static void main(String[] args) throws Exception {
    TC = Integer.parseInt(br.readLine());
    
    for (int t=1; t<=TC; t++) {
      solveTestCase();
      sb.append("#").append(t).append(" ").append(answer).append("\n");
    }
    System.out.print(sb.toString());
  }
}