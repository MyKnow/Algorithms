import java.io.*;
import java.util.*;

public class Main {
  static int N, M;
  static int[] nums;
  static boolean[] used;
  static int[] arr;
  static StringBuilder sb = new StringBuilder();

  static void dfs(int depth) {
    if (depth == M) {
      for (int i=0; i<M; i++) sb.append(arr[i]).append(" ");
      sb.append("\n");
      return;
    }
    
    for (int i=0; i<N; i++) {
      if (used[i]) continue;
      used[i] = true;
      arr[depth] = nums[i];
      dfs(depth+1);
      used[i] = false;
    }
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    nums = new int[N];
    arr = new int[M];
    
    st = new StringTokenizer(br.readLine());
    for (int i=0; i<N; i++) {
      nums[i] = Integer.parseInt(st.nextToken());
    }
    
    Arrays.sort(nums);

    used = new boolean[N];
    dfs(0);
    System.out.print(sb);
  }
}
