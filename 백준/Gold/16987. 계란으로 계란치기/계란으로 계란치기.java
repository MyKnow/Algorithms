import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int N;
  static int[] S;
  static int[] W;

  static int maxBroken = 0;

  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    S = new int[N];
    W = new int[N];

    for (int i=0; i<N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      S[i] = Integer.parseInt(st.nextToken());
      W[i] = Integer.parseInt(st.nextToken());
    }
  }

  static void dfs(int idx) {
    if (idx == N) {
      int count = 0;
      for (int i=0; i<N; i++) if (S[i] <= 0) count++;
      maxBroken = Math.max(maxBroken, count);
      return;
    }

    // 이미 깨진 계란이면 다음 인덱스로 이동
    if (S[idx] <= 0) {
      dfs(idx+1);
      return;
    }

    boolean hit = false;

    // 현재 들고 있는 계란을 제외하고, 깨지지 않은 계란을 모두 친다.
    for (int i=0; i<N; i++) {
      if (i == idx || S[i] <= 0) continue;

      S[idx] -= W[i];
      S[i] -= W[idx];

      dfs(idx+1);

      S[idx] += W[i];
      S[i] += W[idx];

      hit = true;
    }

    if (!hit) dfs(idx+1);
  }

  public static void main(String[] args) throws Exception {
    init();
    dfs(0);
    sb.append(maxBroken).append("\n");
    System.out.print(sb);
  }
}
