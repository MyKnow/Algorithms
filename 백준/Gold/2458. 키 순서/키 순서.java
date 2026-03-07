import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int N, M;
  static boolean[][] graph;
  static int answer;

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    graph = new boolean[N+1][N+1];

    for (int i=0; i<M; i++) {
      st = new StringTokenizer(br.readLine());

      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());

      graph[from][to] = true;
    }
  }

  static void solve() {
    floydWarshall();

    for (int i=1; i<=N; i++) {
      int count = 0;
      for (int j=1; j<=N; j++) {
        if (graph[i][j] || graph[j][i]) {
          count++;
        }
      }
      if (count == N-1) answer++;
    }

    sb.append(answer);
  }
  
  static void floydWarshall() {
    for (int k=1; k<=N; k++) {
      for (int i=1; i<=N; i++) {
        if (!graph[i][k]) continue;

        for (int j=1; j<=N; j++) {
          if (graph[k][j]) {
            graph[i][j] = true;
          }
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}