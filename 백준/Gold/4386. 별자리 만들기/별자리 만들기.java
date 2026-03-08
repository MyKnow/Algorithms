import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static double sum;
  
  static int N;
  static double[] x, y;
  static boolean[] visited;
  static double[] minDist;
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    
    x = new double[N];
    y = new double[N];
    
    for (int i=0; i<N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      x[i] = Double.parseDouble(st.nextToken());
      y[i] = Double.parseDouble(st.nextToken());
    }
    
    visited = new boolean[N];
    minDist = new double[N];
    
    Arrays.fill(minDist, Double.MAX_VALUE);
    minDist[0] = 0;
  }
  
  static void solve() {
    for (int i=0; i<N; i++) {
      int u = -1;
      double min = Double.MAX_VALUE;
      
      for (int j=0; j<N; j++) {
        if (!visited[j] && minDist[j] < min) {
          min = minDist[j];
          u = j;
        }
      }
      
      visited[u] = true;
      sum += min;
      
      for (int v=0; v<N; v++) {
        if (!visited[v]) {
          double dx = x[u] - x[v];
          double dy = y[u] - y[v];
          double dist = Math.sqrt(dx*dx + dy*dy);
          
          if (dist < minDist[v]) {
            minDist[v] = dist;
          }
        }
      }
    }
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    
    sb.append(String.format("%.2f", sum)).append("\n");
    System.out.print(sb.toString());
  }
}