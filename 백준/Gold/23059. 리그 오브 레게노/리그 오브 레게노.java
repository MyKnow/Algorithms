import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int N, processed;
  static Map<String, List<String>> graph;
  static Map<String, Integer> indegree;

  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());

    graph = new HashMap<>();
    indegree = new HashMap<>();

    for (int i = 0; i < N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      String A = st.nextToken();
      String B = st.nextToken();

      graph.putIfAbsent(A, new ArrayList<>());
      graph.putIfAbsent(B, new ArrayList<>());
      indegree.putIfAbsent(A, 0);
      indegree.putIfAbsent(B, 0);

      graph.get(A).add(B);
      indegree.put(B, indegree.get(B) + 1);
    }

    processed = 0;
  }

  static void solve() {
    List<String> currentLevel = new ArrayList<>();

    for (String key : indegree.keySet()) {
      if (indegree.get(key) == 0) {
        currentLevel.add(key);
      }
    }

    while (!currentLevel.isEmpty()) {
      Collections.sort(currentLevel);

      List<String> nextLevel = new ArrayList<>();

      for (String current : currentLevel) {
        sb.append(current).append("\n");
        processed++;

        for (String next : graph.get(current)) {
          indegree.put(next, indegree.get(next) - 1);
          if (indegree.get(next) == 0) {
            nextLevel.add(next);
          }
        }
      }

      currentLevel = nextLevel;
    }
  }

  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.println(processed != indegree.size() ? -1 : sb.toString());
  }
}