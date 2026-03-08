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
  static long K, sum;

  static int[] parent;
  static List<Edge> edges;

  static class Edge implements Comparable<Edge> {
    int u, v;
    long w;

    Edge(int u, int v, long w) {
      this.u = u;
      this.v = v;
      this.w = w;
    }
    
    @Override
    public int compareTo(Edge e) {
      return Long.compare(this.w, e.w);
    }
  }

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    K = Long.parseLong(st.nextToken());

    parent = new int[N+1];
    for (int i=1;i<=N;i++) parent[i] = i-1;
    parent[1] = N;

    st = new StringTokenizer(br.readLine());
    edges = new ArrayList<>();
    for (int i=1;i<=N;i++) {
      long w = Long.parseLong(st.nextToken());
      edges.add(new Edge(0, i, w));
    }

    for (int i=0;i<M;i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      int min = Math.min(a,b);
      int max = Math.max(a,b);

      if (min==1 && max==N) {
        parent[1] = 1;
        continue;
      }

      parent[max] = max;
    }
    
    sum = 0;
  }

  static int find(int x) {
    if (parent[x]==x) return x;
    return parent[x] = find(parent[x]);
  }

  static boolean union(int a,int b) {
    a = find(a);
    b = find(b);
    if (a==b) return false;
    parent[a] = b;
    return true;
  }

  static void solve() {
    if (M<=1) {
      sb.append("YES");
      return;
    }
    
    Collections.sort(edges);
    for (Edge e: edges) {
      if (union(e.u, e.v)) sum += e.w;
    }
    
    sb.append(sum<=K ? "YES" : "NO");
  }

  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.println(sb.toString());
  }
}