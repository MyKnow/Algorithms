import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Arrays;

public class Main {
  final static int MAX = Integer.MAX_VALUE / 100;
  
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int answer;
  static int S;
  static int N, E;
  static int U, V;
  static List<Edge>[] edge;
  
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
    E = Integer.parseInt(st.nextToken());
    
    edge = new ArrayList[N+1];
    for (int i=1; i<=N; i++) edge[i] = new ArrayList<>();
    
    for (int e=0; e<E; e++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int c = Integer.parseInt(st.nextToken());
      
      edge[a].add( new Edge(b, c) );
      edge[b].add( new Edge(a, c) );
    }
    
    st = new StringTokenizer(br.readLine());
    U = Integer.parseInt(st.nextToken());
    V = Integer.parseInt(st.nextToken());
    S = 1;

    answer = MAX;
  }
  
  static void solve() {
    int[] dijkstraS = dijkstra(S);
    int[] dijkstraU = dijkstra(U);
    int[] dijkstraV = dijkstra(V);
    
    int path1 = dijkstraS[U] + dijkstraU[V] + dijkstraV[N];
    int path2 = dijkstraS[V] + dijkstraV[U] + dijkstraU[N];
    
    if (path1 >= MAX && path2 >= MAX) answer = -1;
    else answer = Math.min(path1, path2);
  }
  
  static int[] dijkstra(int start) {
    PriorityQueue<Edge> pq = new PriorityQueue<>();
    pq.add( new Edge(start, 0) );
    
    int[] dist = new int[N+1];
    Arrays.fill(dist, MAX);
    dist[start] = 0;
    
    while(!pq.isEmpty()) {
      Edge cur = pq.poll();
      
      if (cur.dist > dist[cur.to]) continue;
      
      for (Edge next: edge[cur.to]) {
        int nextDist = cur.dist + next.dist;
        
        if (nextDist > dist[next.to]) continue;
        
        dist[next.to] = nextDist;
        pq.add( new Edge(next.to, nextDist) );
      }
    }
    
    return dist;
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    sb.append(answer).append("\n");
    System.out.print(sb.toString());
  }
}