import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 결론, 나보다 적거나 같은 비용의 주유소에 도달할 정도의 기름만 채우자!

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int answer;
  
  static int stationsSize;
  static int roadsSize;
  static int[] roads;
  static int[] stations;
  
  
  static void init() throws Exception {
    stationsSize = Integer.parseInt(br.readLine());
    roadsSize = stationsSize-1;
    
    roads = new int[roadsSize];
    stations = new int[stationsSize];
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i=0; i<roadsSize; i++) {
      roads[i] = Integer.parseInt(st.nextToken());
    }
    
    st = new StringTokenizer(br.readLine());
    for (int i=0; i<stationsSize; i++) {
      stations[i] = Integer.parseInt(st.nextToken());
    }
    
    answer = 0;
  }
  
  static void solve() {
    int currentPrice = stations[0];
    for (int i=0; i<roadsSize; i++) {
      currentPrice = Math.min(currentPrice, stations[i]);
      int currentDistance = roads[i];
      answer += currentPrice * currentDistance;
    }
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    sb.append(answer).append("\n");
    System.out.print(sb.toString());
  }
}