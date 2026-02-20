import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.List;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int N, M;
  static List<Integer>[] graph;
  static int[] indegree;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    
    graph = new ArrayList[N+1];
    indegree = new int[N+1];
    
    for (int i=1; i<=N; i++) {
      graph[i] = new ArrayList<>();
    }
    
    for (int i=0; i<M; i++) {
      st = new StringTokenizer(br.readLine());
      int A = Integer.parseInt(st.nextToken());
      int B = Integer.parseInt(st.nextToken());
      
      graph[A].add(B);
      indegree[B]++;
    }
  }
  
  static void bfs() {
    ArrayDeque<Integer> q = new ArrayDeque<>();
    
    for (int i=1; i<=N; i++) {
      if (indegree[i] == 0) {
        q.addLast(i);
      }
    }
    
    while (!q.isEmpty()) {
      int current = q.pollFirst();
      sb.append(current).append(" ");
      
      for (int next : graph[current]) {
        indegree[next]--;
        if (indegree[next] == 0) {
          q.addLast(next);
        }
      }
    }
  }
  
  public static void main(String[] args) throws Exception {
    init();
    bfs();
    sb.append("\n");
    System.out.print(sb.toString());
  }
}