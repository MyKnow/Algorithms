import java.util.*;
import java.io.*;

public class Main {
  static int computerSize, graphSize;
  static boolean[][] graph;
  static boolean[] visited;
  
  static int dfs(int src) {
    int count = 0;
    Deque<Integer> dq = new ArrayDeque<>();
    dq.addLast(src);
    visited[src] = true;
    
    while (!dq.isEmpty()) {
      Integer top = dq.pollLast();
      for (int dst=1; dst<=computerSize; dst++) {
        if (!visited[dst] && graph[top][dst]) {
          visited[dst] = true;
          count++;
          dq.addLast(dst);
        }
      }
    }
    return count;
  }
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    computerSize = Integer.parseInt(br.readLine());
    graphSize = Integer.parseInt(br.readLine());
    
    graph = new boolean[computerSize+1][computerSize+1];
    visited = new boolean[computerSize+1];
    for (int i=0; i<graphSize; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int src = Integer.parseInt(st.nextToken());
      int dst = Integer.parseInt(st.nextToken());
      
      graph[src][dst] = true;
      graph[dst][src] = true;
    }
    
    System.out.println(dfs(1));
  }
}