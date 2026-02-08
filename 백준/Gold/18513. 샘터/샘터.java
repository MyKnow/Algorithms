import java.io.*;
import java.util.*;

public class Main {

  static class Node {
    // 위치
    long x;
    // 가장 가까운 샘터까지의 거리
    long dist;

    Node(long x, long dist) {
      this.x = x;
      this.dist = dist;
    }
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int K = Integer.parseInt(st.nextToken());
    int N = Integer.parseInt(st.nextToken());

    // 방문 체크용 (샘터 + 이미 집 지은 위치)
    HashSet<Long> visited = new HashSet<>();

    // BFS 큐
    Queue<Node> q = new ArrayDeque<>();

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < K; i++) {
      long x = Long.parseLong(st.nextToken());
      q.offer(new Node(x, 0));
      visited.add(x);
    }

    long answer = 0;
    int built = 0;
    
    while (!q.isEmpty()) {
      Node cur = q.poll();

      for (int d = -1; d <= 1; d += 2) {
        long nx = cur.x + d;

        if (visited.contains(nx)) continue;

        visited.add(nx);
        built++;
        answer += cur.dist + 1;

        if (built == N) {
          System.out.println(answer);
          return;
        }

        q.offer(new Node(nx, cur.dist + 1));
      }
    }
  }
}
