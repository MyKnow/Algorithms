import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int answer;
  
  static int M, N;
  static int[] parent;
  static List<Edge> edge;
  static int cost;
  
  static class Edge implements Comparable<Edge> {
    int x, y, z;
    
    Edge(int x, int y, int z) {
      this.x = x;
      this.y = y;
      this.z = z;
    }
    
    @Override
    public int compareTo(Edge e) {
      return Integer.compare(this.z, e.z);
    }
  }
  
  static boolean init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    M = Integer.parseInt(st.nextToken());
    N = Integer.parseInt(st.nextToken());
    
    if (M == 0) return false;
    
    parent = new int[M];
    cost = 0;
    edge = new ArrayList<>();
    
    for (int i=0; i<M; i++) parent[i] = i;
    
    for (int i=0; i<N; i++) {
      st = new StringTokenizer(br.readLine());
      
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      int z = Integer.parseInt(st.nextToken());
      edge.add( new Edge(x, y, z) );
      cost += z;
    }
    
    answer = 0;
    
    return true;
  }
  
  static void solve() {
    Collections.sort(edge);
    
    int count = 0;
    for (Edge e: edge) {
      if (union(e.x, e.y)) {
        answer += e.z;
        if (count++ == M-1) break;
      }
    }
    
    answer = cost - answer;
    sb.append(answer).append("\n");
  }
  
  static boolean union(int a, int b) {
    a = find(a);
    b = find(b);
    
    if (a == b) return false;
    
    parent[b] = a;
    return true;
  }
  
  static int find(int x) {
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
  }
  
  public static void main(String[] args) throws Exception {
    while(init()) {
      solve();
    }
    System.out.print(sb.toString());
  }
}