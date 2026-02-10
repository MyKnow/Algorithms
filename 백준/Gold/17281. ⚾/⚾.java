import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  static int N;
  static int[][] hit;
  static int[] order;
  static boolean[] used;

  static int answer;

  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());

    hit = new int[N][9];
    for (int i = 0; i < N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j = 0; j < 9; j++) {
        hit[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    order = new int[9];
    used = new boolean[9];

    order[3] = 0;
    used[0] = true;

    answer = 0;
  }

  static void dfs(int depth) {
    if (depth == 9) {
      answer = Math.max(answer, simulate());
      return;
    }

    if (depth == 3) {
      dfs(depth + 1);
      return;
    }

    for (int i = 1; i < 9; i++) {
      if (used[i]) continue;

      used[i] = true;
      order[depth] = i;
      dfs(depth + 1);
      used[i] = false;
    }
  }

  static int simulate() {
    int score = 0;
    int idx = 0;

    for (int inning = 0; inning < N; inning++) {
      int out = 0;
      int base = 0;

      while (out < 3) {
        int player = order[idx];
        int result = hit[inning][player];

        if (result == 0) {
          out++;
        }
        else if (result == 4) {
          score += Integer.bitCount(base) + 1;
          base = 0;
        }
        else {
          base = (base << result) | (1 << (result - 1));
          score += Integer.bitCount(base >> 3);
          base &= 0b111;
        }

        idx++;
        if (idx == 9) idx = 0;
      }
    }
    return score;
  }

  public static void main(String[] args) throws Exception {
    init();
    dfs(0);
    System.out.print(answer);
  }
}
