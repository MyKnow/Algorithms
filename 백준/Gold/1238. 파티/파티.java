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
  static int[][] minDist;
  
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
    minDist = new int[N+1][N+1];
    for (int i=1; i<=N; i++) {
      edge[i] = new ArrayList<>();
      Arrays.fill(minDist[i], Integer.MAX_VALUE);
    }
    
    for (int i=0; i<M; i++) {
      st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      int dist = Integer.parseInt(st.nextToken());
      
      edge[from].add( new Edge(to, dist) ); 
    }
  }
  
  static void solve() {
    for (int i=1; i<=N; i++) {
      dijkstra(i);
    }
    
    int answer = 0;
    for (int i=1; i<=N; i++) {
      answer = Math.max(answer, minDist[i][X] + minDist[X][i]);
    }
    sb.append(answer).append("\n");
  }
  
  static void dijkstra(int start) {
    PriorityQueue<Edge> pq = new PriorityQueue<>();
    pq.add( new Edge(start, 0) );
    minDist[start][start] = 0;
    
    while(!pq.isEmpty()) {
      Edge cur = pq.poll();
      int curDist = cur.dist;
      
      if (curDist < minDist[start][cur.to]) {
        minDist[start][cur.to] = curDist;
      }
      
      for (Edge next: edge[cur.to]) {
        int nextDist = curDist + next.dist;
        
        if (nextDist >= minDist[start][next.to]) continue;
        pq.add( new Edge(next.to, nextDist) );
      }
    }
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}