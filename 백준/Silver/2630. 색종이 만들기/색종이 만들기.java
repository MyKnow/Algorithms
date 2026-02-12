import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int N;
  static boolean[][] paper; // true: 파란색, false: 흰색

  static int bCount = 0;
  static int wCount = 0;

  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    paper = new boolean[N][N];

    for (int r = 0; r < N; r++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int c = 0; c < N; c++) {
        paper[r][c] = Integer.parseInt(st.nextToken()) == 1;
      }
    }
  }

  static void solution(int n, boolean[][] m) {
    boolean allBlue = true;
    boolean allWhite = true;

    for (int r = 0; r < n; r++) {
      for (int c = 0; c < n; c++) {
        if (m[r][c]) allWhite = false;
        else allBlue = false;
      }
    }

    if (allBlue) bCount++;
    else if (allWhite) wCount++;
    else {
      boolean[][][] divided = divide(n, m);
      for (int i = 0; i < 4; i++) {
        solution(n/2, divided[i]);
      }
    }
  }

  static boolean[][][] divide(int n, boolean[][] m) {
    int half = n / 2;
    boolean[][] topLeft = new boolean[half][half];
    boolean[][] topRight = new boolean[half][half];
    boolean[][] botLeft = new boolean[half][half];
    boolean[][] botRight = new boolean[half][half];

    for (int r = 0; r < n; r++) {
      for (int c = 0; c < n; c++) {
        if (r < half && c < half) topLeft[r][c] = m[r][c];
        else if (r < half && c >= half) topRight[r][c-half] = m[r][c];
        else if (r >= half && c < half) botLeft[r-half][c] = m[r][c];
        else botRight[r-half][c-half] = m[r][c];
      }
    }

    return new boolean[][][]{ topLeft, topRight, botLeft, botRight };
  }

  public static void main(String[] args) throws Exception {
    init();
    solution(N, paper);
    sb.append(wCount).append("\n").append(bCount).append("\n");
    System.out.print(sb);
  }
}
