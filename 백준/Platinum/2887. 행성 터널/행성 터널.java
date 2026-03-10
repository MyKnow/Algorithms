import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int N;
  static long answer;
  
  static Planet[] planet;
  static int[] parent;
  static List<Edge> edge;
  
  static class Planet {
    int idx, x, y, z;
    
    Planet(int idx, int x, int y, int z) {
      this.idx = idx;
      this.x = x;
      this.y = y;
      this.z = z;
    }
  }
  
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
    N = Integer.parseInt(br.readLine());
    
    planet = new Planet[N];
    
    for (int i=0; i<N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      int z = Integer.parseInt(st.nextToken());
      
      planet[i] = new Planet(i, x, y, z);
    }
    
    parent = new int[N];
    for (int i=0; i<N; i++) parent[i] = i;
    
    edge = new ArrayList<>();
  }
  
  static void solve() {
    Collections.sort(Arrays.asList(planet), (a,b) -> a.x - b.x);
    for (int i=0; i<N-1; i++) {
      int cost = Math.abs(planet[i].x - planet[i+1].x);
      edge.add(new Edge(planet[i].idx, planet[i+1].idx, cost));
    }
    
    Collections.sort(Arrays.asList(planet), (a,b) -> a.y - b.y);
    for (int i=0; i<N-1; i++) {
      int cost = Math.abs(planet[i].y - planet[i+1].y);
      edge.add(new Edge(planet[i].idx, planet[i+1].idx, cost));
    }
    
    Collections.sort(Arrays.asList(planet), (a,b) -> a.z - b.z);
    for (int i=0; i<N-1; i++) {
      int cost = Math.abs(planet[i].z - planet[i+1].z);
      edge.add(new Edge(planet[i].idx, planet[i+1].idx, cost));
    }
    
    Collections.sort(edge);
    
    int count = 0;
    for (Edge e : edge) {
      if (union(e.u, e.v)) {
        answer += e.w;
        count++;
        if (count == N-1) break;
      }
    }
    sb.append(answer).append("\n");
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