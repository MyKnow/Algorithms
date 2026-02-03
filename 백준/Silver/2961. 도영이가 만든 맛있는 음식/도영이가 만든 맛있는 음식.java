import java.util.*;
import java.io.*;

// 신맛은 곱
// 쓴맛은 합
// 재료의 개수는 10개 이하의 자연수
// 

public class Main {
  static int N;
  static int[] S;
  static int[] B;
  static int min = Integer.MAX_VALUE;
  static int sTotal;
  static int bTotal;
  
  static void backtracking(int idx, int used) {
    if (idx == N) {
        if (used > 0) {
            min = Math.min(min, Math.abs(sTotal - bTotal));
        }
        return;
    }

    // 선택
    sTotal *= S[idx];
    bTotal += B[idx];
    backtracking(idx + 1, used + 1);
    sTotal /= S[idx];
    bTotal -= B[idx];

    // 비선택
    backtracking(idx + 1, used);
}
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    S = new int[N];
    sTotal = 1;
    B = new int[N];
    bTotal = 0;
    
    for (int i=0; i<N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      S[i] = Integer.parseInt(st.nextToken());
      B[i] = Integer.parseInt(st.nextToken());
    }
    
    backtracking(0, 0);
    
    System.out.print(min);
  }
}
