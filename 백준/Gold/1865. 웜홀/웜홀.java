import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int TC, N, M, W;
  static boolean answer;
  
  static class Edge {
    int from, to, time;
    
    Edge(int from, int to, int time) {
      this.from = from;
      this.to = to;
      this.time = time;
    }
  }
  
  static List<Edge> edges;
  
  static void init() throws Exception {
    answer = false;
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    W = Integer.parseInt(st.nextToken());
    
    edges = new ArrayList<>();
    
    for (int m = 0; m < M; m++) {
      st = new StringTokenizer(br.readLine());
      int S = Integer.parseInt(st.nextToken());
      int E = Integer.parseInt(st.nextToken());
      int T = Integer.parseInt(st.nextToken());
      
      edges.add(new Edge(S, E, T));
      edges.add(new Edge(E, S, T));
    }
    
    for (int w = 0; w < W; w++) {
      st = new StringTokenizer(br.readLine());
      int S = Integer.parseInt(st.nextToken());
      int E = Integer.parseInt(st.nextToken());
      int T = Integer.parseInt(st.nextToken());
      
      edges.add(new Edge(S, E, -T));
    }
  }
  
  static void solve() {
    int[] dist = new int[N + 1];
    
    for (int i = 1; i <= N; i++) {
      dist[i] = 0;
    }
    
    for (int i = 1; i <= N; i++) {
      for (Edge edge : edges) {
        if (dist[edge.to] > dist[edge.from] + edge.time) {
          dist[edge.to] = dist[edge.from] + edge.time;
          if (i == N) {
            answer = true;
            return;
          }
        }
      }
    }
  }
  
  public static void main(String[] args) throws Exception {
    TC = Integer.parseInt(br.readLine());
    
    for (int t = 0; t < TC; t++) {
      init();
      solve();
      sb.append(answer ? "YES" : "NO").append("\n");
    }
    System.out.print(sb.toString());
  }
}