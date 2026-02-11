import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T, answer;
  
  static int maxHeight;
  static int N;
  static int[] trees;
  static int odd;
  static int even;
  static int sum;
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    trees = new int[N];
    maxHeight = 0;
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i=0; i<N; i++) {
      int height = Integer.parseInt(st.nextToken());
      trees[i] = height;
      
      maxHeight = Math.max(maxHeight, height);
    }
    odd = even = sum = answer = 0;
  }
  
  static void solveTestCase() {
    for (int i=0; i<N; i++) {
      int diff = maxHeight-trees[i];
      if (diff % 2 == 1) {
        odd++;
      }
      even += diff/2;
      sum += diff;
    }
    
    if (odd>even) {
      answer = odd*2-1;
    } else {
      answer = (sum/3) * 2 + sum%3;
    }
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t=1; t<=T; t++) {
      init();
      solveTestCase();
      sb.append("#").append(t).append(" ").append(answer).append("\n");
    }
    System.out.print(sb.toString());
  }
}