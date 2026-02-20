import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int answer;
  
  static int T, N, D, C;
  static List<Edge>[] vertex;
  static class Edge {
    int to, time;
    
    Edge(int to, int time) {
      this.to = to;
      this.time = time;
    }
  }
  static int sComputer, sTime;
  static int[] cost;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    D = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
    
    vertex = new ArrayList[N+1];
    for (int d=0; d<D; d++) {
      st = new StringTokenizer(br.readLine());
      int A = Integer.parseInt(st.nextToken());
      int B = Integer.parseInt(st.nextToken());
      int S = Integer.parseInt(st.nextToken());
      
      if (vertex[B] == null) {
        vertex[B] = new ArrayList<>();
      }
      vertex[B].add( new Edge(A, S) );
    }
    cost = new int[N+1];
    Arrays.fill(cost, Integer.MAX_VALUE);
    
    sComputer = 1;
    sTime = 0;
  }
  
  static void solve() {
    PriorityQueue<Edge> pq = new PriorityQueue<>((a, b) -> a.time - b.time);
  
    pq.add(new Edge(C, 0));
    cost[C] = 0;
  
    while (!pq.isEmpty()) {
      Edge current = pq.poll();
  
      if (current.time > cost[current.to]) continue;
  
      if (vertex[current.to] == null) continue;
  
      for (Edge edge : vertex[current.to]) {
        int newCost = current.time + edge.time;
  
        if (newCost < cost[edge.to]) {
          cost[edge.to] = newCost;
          pq.add(new Edge(edge.to, newCost));
        }
      }
    }
  
    sComputer = 0;
    sTime = 0;
  
    for (int i = 1; i <= N; i++) {
      if (cost[i] != Integer.MAX_VALUE) {
        sComputer++;
        sTime = Math.max(sTime, cost[i]);
      }
    }
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t=0; t<T; t++) {
      init();
      solve();
      sb.append(sComputer).append(" ").append(sTime).append("\n");
    }
    System.out.print(sb.toString());
  }
}