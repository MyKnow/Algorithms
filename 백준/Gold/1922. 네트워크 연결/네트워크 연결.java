import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int sum;
  
  static int N;
  static int M;
  static int[] parent;
  static List<Edge> edge;
  
  static class Edge implements Comparable<Edge> {
    int u, v, w;
    
    Edge(int u, int v, int w) {
      this.u = u;
      this.v = v;
      this.w = w;
    }
    
    public int compareTo(Edge e) {
      return Integer.compare(this.w, e.w);
    }
  }
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    M = Integer.parseInt(br.readLine());
    
    parent = new int[N+1];
    for (int i=1; i<=N; i++) parent[i] = i;
    
    edge = new ArrayList<>();
    for (int i=0; i<M; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      int weight = Integer.parseInt(st.nextToken());
      
      edge.add( new Edge(from, to, weight) );
    }
  }
  
  static void solve() {
    int count = 0;
    Collections.sort(edge);
    for (Edge e: edge) {
      if (union(e.u, e.v)) {
        sum += e.w;
        count += 1;
      }
      
      if (count > N-1) break;
    }
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
    sb.append(sum).append("\n");
    System.out.print(sb.toString());
  }
}