import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int T, N, M, C;
  static int[][] map;
  static int[][] profit;

  static int curMax;
  static int[] temp; // 현재 구간의 M개 값

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());

    map = new int[N][N];
    profit = new int[N][N];

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        map[i][j] = Integer.parseInt(st.nextToken());
      }
    }
  }

  // 부분집합 DFS
  static void dfs(int idx, int sum, int val) {
    if (sum > C) return;

    if (idx == M) {
      curMax = Math.max(curMax, val);
      return;
    }

    // 선택
    dfs(idx + 1,
        sum + temp[idx],
        val + temp[idx] * temp[idx]);

    // 미선택
    dfs(idx + 1, sum, val);
  }

  static int calcProfit(int r, int c) {
    temp = new int[M];
    for (int i = 0; i < M; i++) {
      temp[i] = map[r][c + i];
    }

    curMax = 0;
    dfs(0, 0, 0);
    return curMax;
  }

  static int solve() {
    // 1단계: 각 구간의 최대 이익
    for (int i = 0; i < N; i++) {
      for (int j = 0; j <= N - M; j++) {
        profit[i][j] = calcProfit(i, j);
      }
    }

    int answer = 0;

    // 2단계: 두 구간 선택
    for (int i1 = 0; i1 < N; i1++) {
      for (int j1 = 0; j1 <= N - M; j1++) {
        for (int i2 = i1; i2 < N; i2++) {
          for (int j2 = 0; j2 <= N - M; j2++) {

            // 같은 행에서 겹치면 제외
            if (i1 == i2 && j2 < j1 + M && j1 < j2 + M) continue;

            int sum = profit[i1][j1] + profit[i2][j2];
            answer = Math.max(answer, sum);
          }
        }
      }
    }
    return answer;
  }

  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());

    for (int t = 1; t <= T; t++) {
      init();
      int result = solve();
      sb.append("#").append(t).append(" ").append(result).append("\n");
    }
    System.out.print(sb.toString());
  }
}