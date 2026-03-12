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
  
  static int N, M, answer;
  static List<Edge>[] edge;
  static int[] minCost;
  static int src, dst;
  
  static class Edge implements Comparable<Edge> {
    int to, cost;
    
    Edge(int to, int cost) {
      this.to = to;
      this.cost = cost;
    }
    
    @Override
    public int compareTo(Edge e) {
      return Integer.compare(this.cost, e.cost);
    }
  }
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    M = Integer.parseInt(br.readLine());
    
    edge = new ArrayList[N+1];
    for (int i=1; i<=N; i++) {
      edge[i] = new ArrayList<>();
    }
    
    minCost = new int[N+1];
    for (int i=0; i<M; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      int cost = Integer.parseInt(st.nextToken());
      edge[from].add( new Edge(to, cost) );
    }
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    src = Integer.parseInt(st.nextToken());
    dst = Integer.parseInt(st.nextToken());
    
    Arrays.fill(minCost, Integer.MAX_VALUE);
    answer = Integer.MAX_VALUE;
  }
  
  static void solve() {
    dijkstra(src);
    sb.append(answer).append("\n");
  }
  
  static void dijkstra(int start) {
    PriorityQueue<Edge> pq = new PriorityQueue<>();
    pq.add( new Edge(start, 0) );
    minCost[start] = 0;
    
    while(!pq.isEmpty()) {
      Edge cur = pq.poll();
      int curCost = cur.cost;
      
      if (cur.to == dst) {
        answer = Math.min(answer, minCost[cur.to]);
        continue;
      }
      
      if (curCost >= answer) continue;
      
      for (Edge next: edge[cur.to]) {
        int nextCost = curCost + next.cost;
        
        if (minCost[next.to] > nextCost) {
          minCost[next.to] = nextCost;
          pq.add( new Edge(next.to, nextCost) );
        }
      }
    }
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}