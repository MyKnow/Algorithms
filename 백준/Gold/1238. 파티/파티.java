import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int N, M, X;
  static List<Edge>[] edge;
  static List<Edge>[] reverseEdge;
  
  static int[] distFromX;
  static int[] distToX;
  
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
    X = Integer.parseInt(st.nextToken());
    
    edge = new ArrayList[N+1];
    reverseEdge = new ArrayList[N+1];
    
    for (int i=1; i<=N; i++) {
      edge[i] = new ArrayList<>();
      reverseEdge[i] = new ArrayList<>();
    }
    
    for (int i=0; i<M; i++) {
      st = new StringTokenizer(br.readLine());
      
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      int dist = Integer.parseInt(st.nextToken());
      
      edge[from].add(new Edge(to, dist));
      reverseEdge[to].add(new Edge(from, dist));
    }
  }
  
  static void solve() {
    distFromX = dijkstra(edge, X);
    distToX = dijkstra(reverseEdge, X);
    
    int answer = 0;
    for (int i=1; i<=N; i++) {
      answer = Math.max(answer, distFromX[i] + distToX[i]);
    }
    
    sb.append(answer).append("\n");
  }
  
  static int[] dijkstra(List<Edge>[] graph, int start) {
    int[] dist = new int[N+1];
    Arrays.fill(dist, Integer.MAX_VALUE);
    
    PriorityQueue<Edge> pq = new PriorityQueue<>();
    pq.add(new Edge(start, 0));
    dist[start] = 0;
    
    while (!pq.isEmpty()) {
      Edge cur = pq.poll();
      
      if (cur.dist > dist[cur.to]) continue;
      
      for (Edge next : graph[cur.to]) {
        int nextDist = cur.dist + next.dist;
        
        if (nextDist >= dist[next.to]) continue;
        
        dist[next.to] = nextDist;
        pq.add(new Edge(next.to, nextDist));
      }
    }
    
    return dist;
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}