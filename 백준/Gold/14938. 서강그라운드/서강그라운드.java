import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Arrays;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int N, M, R;
  static int answer;
  
  static int[] item;
  static List<Edge>[] graph;
  
  static class Edge implements Comparable<Edge> {
    int v, w;
    
    Edge(int v, int w) {
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
    
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    R = Integer.parseInt(st.nextToken());
    
    item = new int[N+1];
    
    st = new StringTokenizer(br.readLine());
    for (int i=1; i<=N; i++) {
      item[i] = Integer.parseInt(st.nextToken());
    }
    
    graph = new ArrayList[N+1];
    for (int i=1; i<=N; i++) graph[i] = new ArrayList<>();
    
    for (int i=0; i<R; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int l = Integer.parseInt(st.nextToken());
      
      graph[a].add(new Edge(b, l));
      graph[b].add(new Edge(a, l));
    }
  }
  
  static void solve() {
    for (int start=1; start<=N; start++) {
      int sum = dijkstra(start);
      answer = Math.max(answer, sum);
    }
    sb.append(answer).append("\n");
  }
  
  static int dijkstra(int start) {
    int[] dist = new int[N+1];
    Arrays.fill(dist, Integer.MAX_VALUE);
    
    PriorityQueue<Edge> pq = new PriorityQueue<>();
    
    dist[start] = 0;
    pq.add(new Edge(start, 0));
    
    while (!pq.isEmpty()) {
      Edge cur = pq.poll();
      
      if (cur.w > dist[cur.v]) continue;
      
      for (Edge next : graph[cur.v]) {
        int nd = cur.w + next.w;
        
        if (nd < dist[next.v]) {
          dist[next.v] = nd;
          pq.add(new Edge(next.v, nd));
        }
      }
    }
    
    int sum = 0;
    for (int i=1; i<=N; i++) {
      if (dist[i] <= M) {
        sum += item[i];
      }
    }
    
    return sum;
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}