import java.io.*;
import java.util.*;

public class Main {
  static int N, M;
  static boolean[] used;
  static int[] arr;
  static StringBuilder sb = new StringBuilder();

  static void dfs(int start, int depth) {
    if (depth == M) {
      for (int i=0; i<M; i++) sb.append(arr[i]).append(" ");
      sb.append("\n");
      return;
    }
    
    for (int i=start; i<=N; i++) {
      arr[depth] = i;
      dfs(i, depth+1);
    }
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    used = new boolean[N + 1];
    arr = new int[M];

    dfs(1, 0);
    System.out.print(sb);
  }
}