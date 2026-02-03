import java.util.*;
import java.io.*;

// 산성용액의 특성값: 1~10억
// 알칼리성용액의 특성값: -1~-10억

// 같은 양의 두 용액을 혼합한 용액의 특성값: 각 용액의 합
// 0에 가장 가까운 용액을 만드려고 함.

// 전체 용액의 수는 2이상 100,000 이하

public class Main {
  static int N;
  static int[] solution;
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    solution = new int[N];
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i=0; i<N; i++) {
      solution[i] = Integer.parseInt(st.nextToken());
    }
    
    Arrays.sort(solution);

    int left = 0;
    int right = N - 1;
    int best = Integer.MAX_VALUE;
    int a = 0, b = 0;
    
    while (left < right) {
      int sum = solution[left] + solution[right];
    
      if (Math.abs(sum) < best) {
        best = Math.abs(sum);
        a = solution[left];
        b = solution[right];
      }
    
      if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
    System.out.println(a + " " + b);
  }
}