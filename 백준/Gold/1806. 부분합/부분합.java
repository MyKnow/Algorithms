import java.util.*;
import java.io.*;

public class Main {
  static int N, S;
  static int min;
  static int[] pSum;
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    S = Integer.parseInt(st.nextToken());
    
    st = new StringTokenizer(br.readLine());
    pSum = new int[N+1];
    for (int i=1; i<=N; i++) {
      int currentValue = Integer.parseInt(st.nextToken());
      pSum[i] = pSum[i-1] + currentValue;
    }
    
    int left = 0, right = 0;
    int best = Integer.MAX_VALUE;
    
    while (right <= N) {
      int sum = pSum[right] - pSum[left];
    
      if (sum >= S) {
        best = Math.min(best, right - left);
        left++;
      } else {
        right++;
      }
    }
    System.out.println(best == Integer.MAX_VALUE ? 0 : best);
  }
}