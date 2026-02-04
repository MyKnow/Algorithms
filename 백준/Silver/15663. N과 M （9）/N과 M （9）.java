import java.io.*;
import java.util.*;

public class Main {
  static int N, M;
  static int[] nums;
  static int[] count;
  static int[] arr;
  static int size;
  static StringBuilder sb = new StringBuilder();

  static void dfs(int depth) {
    if (depth == M) {
      for (int i = 0; i < M; i++) sb.append(arr[i]).append(' ');
      sb.append('\n');
      return;
    }

    for (int i = 0; i < size; i++) {
      if (count[i] == 0) continue;

      count[i]--;
      arr[depth] = nums[i];
      dfs(depth + 1);
      count[i]++;
    }
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    int[] input = new int[N];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      input[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(input);


    nums = new int[N];
    count = new int[N];
    size = 0;
    for (int i = 0; i < N; i++) {
      if (i == 0 || input[i] != input[i - 1]) {
        nums[size] = input[i];
        count[size] = 1;
        size++;
      } else {
        count[size - 1]++;
      }
    }

    arr = new int[M];
    dfs(0);
    System.out.print(sb);
  }
}