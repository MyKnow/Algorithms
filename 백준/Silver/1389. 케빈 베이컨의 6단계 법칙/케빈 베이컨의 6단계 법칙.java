import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;
import java.util.Arrays;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int N, M;
  static boolean[][] relation;
  static int[][] graph;

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    relation = new boolean[N+1][N+1];

    for (int i=0; i<M; i++) {
      st = new StringTokenizer(br.readLine());
      int src = Integer.parseInt(st.nextToken());
      int dst = Integer.parseInt(st.nextToken());
      relation[src][dst] = true;
      relation[dst][src] = true;
    }

    graph = new int[N+1][];
    for (int r=1; r<=N; r++) {
      int count = 0;
      int[] tmp = new int[N];
      for (int c=1; c<=N; c++) {
        if (relation[r][c]) tmp[count++] = c;
      }
      graph[r] = Arrays.copyOf(tmp, count);
    }
  }

  static void solve() {
    int minSum = Integer.MAX_VALUE;
    int person = 1;

    for (int i=1; i<=N; i++) {
      int sum = bfs(i);
      if (sum < minSum) {
        minSum = sum;
        person = i;
      }
    }

    sb.append(person).append("\n");
  }

  static int bfs(int start) {
    boolean[] visited = new boolean[N+1];
    int[] dist = new int[N+1];
    Arrays.fill(dist, 0);

    ArrayDeque<Integer> q = new ArrayDeque<>();
    q.add(start);
    visited[start] = true;

    while (!q.isEmpty()) {
      int cur = q.poll();
      for (int next : graph[cur]) {
        if (!visited[next]) {
          visited[next] = true;
          dist[next] = dist[cur] + 1;
          q.add(next);
        }
      }
    }

    int sum = 0;
    for (int i=1; i<=N; i++) sum += dist[i];
    return sum;
  }

  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}