import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T, N, answer;
  static int digitMask;
  
  static void updateDigitMask(int value) {
    while (value > 0) {
      digitMask |= 1 << (value % 10);
      value /= 10;
    }
  }
  
  static boolean isAllChecked() {
    for (int i=0; i<=9; i++) {
      if ((digitMask & (1 << i)) == 0) return false;
    }
    return true;
  }
  
  static void solveTestCase() throws Exception {
    N = Integer.parseInt(br.readLine());
    digitMask = 0;
    int k=1;
    do {
      answer = N*k++;
      updateDigitMask(answer);
    } while(!isAllChecked());
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t=1; t<=T; t++) {
      solveTestCase();
      sb.append("#").append(t).append(" ").append(answer).append("\n");
    }
    System.out.print(sb.toString());
  }
}