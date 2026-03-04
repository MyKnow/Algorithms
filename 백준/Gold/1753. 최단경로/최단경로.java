import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  final static int INF = Integer.MAX_VALUE / 100;
  static int V, E;
  static int K;
  static List<Node>[] nodes;
  static int[] dist;
  
  static class Node implements Comparable<Node> {
    int to, weight;
    
    Node(int to, int weight) {
      this.to = to;
      this.weight = weight;
    }
    
    @Override
    public int compareTo(Node node) {
      return Integer.compare(weight, node.weight);
    }
  }
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    V = Integer.parseInt(st.nextToken());
    E = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(br.readLine());
    
    nodes = new ArrayList[V+1];
    dist = new int[V+1];
    for (int i=1; i<=V; i++) {
      nodes[i] = new ArrayList<>();
      dist[i] = INF;
    }
    
    for (int i=0; i<E; i++) {
      st = new StringTokenizer(br.readLine());
      int u = Integer.parseInt(st.nextToken());
      int v = Integer.parseInt(st.nextToken());
      int w = Integer.parseInt(st.nextToken());
      nodes[u].add(new Node(v, w));
    }
  }
  
  static void solve() {
    dijkstra();
    for (int i = 1; i <= V; i++) {
      if (dist[i] == INF) sb.append("INF\n");
      else sb.append(dist[i]).append('\n');
    }
  }
  
  static void dijkstra() {
    PriorityQueue<Node> pq = new PriorityQueue<>();
    
    dist[K] = 0;
    pq.add(new Node(K, 0));
    
    while (!pq.isEmpty()) {
      Node cur = pq.poll();
      
      if (cur.weight > dist[cur.to]) continue;
      
      for (Node next : nodes[cur.to]) {
        int nextWeight = dist[cur.to] + next.weight;
        
        if (nextWeight < dist[next.to]) {
          dist[next.to] = nextWeight;
          pq.add(new Node(next.to, nextWeight));
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