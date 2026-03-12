import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Arrays;
import java.util.Collections;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int N, M, T;
  static int S, G, H;
  static int ghDist;
  
  static List<Edge>[] edge;
  static int[] X;
  
  static class Edge implements Comparable<Edge> {
    int to, dist;
    
    Edge(int to, int dist) {
      this.to = to;
      this.dist = dist;
    }
    
    @Override
    public int compareTo(Edge e) {
      return Integer.compare(this.dist, e.dist);
    }
  }
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    T = Integer.parseInt(st.nextToken());
    
    st = new StringTokenizer(br.readLine());
    S = Integer.parseInt(st.nextToken());
    G = Integer.parseInt(st.nextToken());
    H = Integer.parseInt(st.nextToken());
    
    edge = new ArrayList[N+1];
    for (int i=1; i<=N; i++) edge[i] = new ArrayList<>();
    
    ghDist = 0;
    
    for (int i=0; i<M; i++) {
      st = new StringTokenizer(br.readLine());
      
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int d = Integer.parseInt(st.nextToken());
      
      edge[a].add(new Edge(b, d));
      edge[b].add(new Edge(a, d));
      
      if ((a == G && b == H) || (a == H && b == G)) {
        ghDist = d;
      }
    }
    
    X = new int[T];
    for (int i=0; i<T; i++) {
      X[i] = Integer.parseInt(br.readLine());
    }
    
    Arrays.sort(X);
  }
  
  static void solve() {
    int[] distS = dijkstra(S);
    int[] distG = dijkstra(G);
    int[] distH = dijkstra(H);
    
    for (int x : X) {
      int path1 = distS[G] + ghDist + distH[x];
      int path2 = distS[H] + ghDist + distG[x];
      
      if (distS[x] == path1 || distS[x] == path2) {
        sb.append(x).append(" ");
      }
    }
    
    sb.append("\n");
  }
  
  static int[] dijkstra(int start) {
    int[] dist = new int[N+1];
    Arrays.fill(dist, Integer.MAX_VALUE);
    
    PriorityQueue<Edge> pq = new PriorityQueue<>();
    pq.add(new Edge(start, 0));
    dist[start] = 0;
    
    while (!pq.isEmpty()) {
      Edge cur = pq.poll();
      
      if (cur.dist > dist[cur.to]) continue;
      
      for (Edge next : edge[cur.to]) {
        int nextDist = cur.dist + next.dist;
        
        if (nextDist < dist[next.to]) {
          dist[next.to] = nextDist;
          pq.add(new Edge(next.to, nextDist));
        }
      }
    }
    
    return dist;
  }
  
  public static void main(String[] args) throws Exception {
    int TC = Integer.parseInt(br.readLine());
    
    for (int t=0; t<TC; t++) {
      init();
      solve();
    }
    
    System.out.print(sb.toString());
  }
}