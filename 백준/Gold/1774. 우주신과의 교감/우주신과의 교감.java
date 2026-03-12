import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int N, M;
  static int[] parent;

  static Coords[] coords;
  static List<Edge> edges;

  static class Coords {
    int x, y;

    Coords(int x, int y) {
      this.x = x;
      this.y = y;
    }

    double getDistanceWith(Coords c) {
      long dx = this.x - c.x;
      long dy = this.y - c.y;
      return Math.sqrt(dx * dx + dy * dy);
    }
  }

  static class Edge implements Comparable<Edge> {
    int u, v;
    double w;

    Edge(int u, int v, double w) {
      this.u = u;
      this.v = v;
      this.w = w;
    }

    @Override
    public int compareTo(Edge e) {
      return Double.compare(this.w, e.w);
    }
  }

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    coords = new Coords[N + 1];
    parent = new int[N + 1];

    for (int i = 1; i <= N; i++) {
      parent[i] = i;
    }

    for (int i = 1; i <= N; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      coords[i] = new Coords(x, y);
    }

    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      union(a, b);
    }
    
    edges = new ArrayList<>();
    for (int i = 1; i <= N; i++) {
      for (int j = i + 1; j <= N; j++) {
        double dist = coords[i].getDistanceWith(coords[j]);
        edges.add( new Edge(i, j, dist) );
      }
    }
  }

  static void solve() {
    Collections.sort(edges);

    double answer = 0;
    int edgeCount = 0;
    
    for (Edge e : edges) {
      if (union(e.u, e.v)) {
        answer += e.w;
        edgeCount++;
        if (edgeCount == N - 1) break;
      }
    }
    sb.append(String.format("%.2f", answer)).append("\n");
  }

  static int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
  }

  static boolean union(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) return false;

    parent[b] = a;
    return true;
  }

  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}