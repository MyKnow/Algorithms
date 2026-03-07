import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int V, E;
  static List<Edge> edges;
  static int[] parent;
  static int answer;

  static class Edge implements Comparable<Edge> {
    int u, v, w;

    Edge(int u, int v, int w) {
      this.u = u;
      this.v = v;
      this.w = w;
    }

    @Override
    public int compareTo(Edge e) {
      return Integer.compare(this.w, e.w);
    }
  }

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());

    V = Integer.parseInt(st.nextToken());
    E = Integer.parseInt(st.nextToken());

    edges = new ArrayList<>();
    parent = new int[V+1];

    for (int i=1;i<=V;i++) parent[i] = i;

    for (int i=0;i<E;i++) {
      st = new StringTokenizer(br.readLine());

      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int c = Integer.parseInt(st.nextToken());

      edges.add(new Edge(a,b,c));
    }
  }

  static int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
  }

  static void union(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) parent[b] = a;
  }

  static void solve() {
    Collections.sort(edges);
    int count = 0;
    for (Edge e : edges) {
      if (find(e.u) != find(e.v)) {
        union(e.u, e.v);
        answer += e.w;
        count++;
        if (count == V-1) break;
      }
    }
    sb.append(answer);
  }

  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}