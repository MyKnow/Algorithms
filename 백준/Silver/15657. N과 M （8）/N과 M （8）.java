import java.util.*;
import java.io.*;

public class Main {
  static int N, M;
  static int[] nums;
  static int[] arr;
  
  static StringBuilder sb = new StringBuilder();
  static void dfs(int start, int depth) {
    if (depth == M) {
      for (int i=0; i<M; i++) sb.append(arr[i]).append(" ");
      sb.append("\n");
      return;
    }
    
    for (int i=start; i<N; i++) {
      arr[depth] = nums[i];
      dfs(i, depth+1);
    }
  }
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    
    st = new StringTokenizer(br.readLine());
    nums = new int[N];
    for (int i=0; i<N; i++) {
      nums[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(nums);
    
    arr = new int[M];
    dfs(0, 0);
    System.out.print(sb.toString());
  }
}