import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Solution {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int sr, sc, er, ec;
  static int dr, dc;
  static int answer;

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());

    sr = Integer.parseInt(st.nextToken());
    sc = Integer.parseInt(st.nextToken());
    er = Integer.parseInt(st.nextToken());
    ec = Integer.parseInt(st.nextToken());

    dr = Math.abs(er - sr);
    dc = Math.abs(ec - sc);
  }

  static void solve() {
    int t = (dr + dc) / 2;
    answer = 2 * t + Math.abs(dr - t) + Math.abs(dc - t);
  }

  public static void main(String[] args) throws Exception {
    int T = Integer.parseInt(br.readLine());

    for (int tc = 1; tc <= T; tc++) {
      init();
      solve();
      sb.append("#").append(tc).append(" ").append(answer).append("\n");
    }

    System.out.print(sb);
  }
}
