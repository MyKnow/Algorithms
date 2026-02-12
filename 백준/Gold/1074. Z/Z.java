import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int N, R, C, size;
  static int answer = 0;

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
    size = 1 << N;
    answer = 0;
  }

  static void z(int size, int sr, int sc) {
    // 1x1 칸
    if (size == 1) { 
      if (sr == R && sc == C) return;
      answer++;
      return;
    }

    int half = size / 2;

    // 좌상
    if (R < sr + half && C < sc + half) {
      z(half, sr, sc);
      return;
    } else answer += half * half;

    // 우상
    if (R < sr + half && C >= sc + half) {
      z(half, sr, sc + half);
      return;
    } else answer += half * half;

    // 좌하
    if (R >= sr + half && C < sc + half) {
      z(half, sr + half, sc);
      return;
    } else answer += half * half;

    // 우하
    z(half, sr + half, sc + half);
  }

  public static void main(String[] args) throws Exception {
    init();
    z(size, 0, 0);
    sb.append(answer).append("\n");
    System.out.print(sb);
  }
}
