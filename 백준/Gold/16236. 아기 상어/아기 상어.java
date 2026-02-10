import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  
  static int N;
  static int[][] ocean;
  static int answer;
  static Shark shark;
  
  static int[] dr = { -1, 0, 0, 1 };
  static int[] dc = {  0,-1, 1, 0 };
  
  static class Shark {
    int r, c;
    int size = 2;
    int eat = 0;
    
    Shark(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    ocean = new int[N][N];
    
    for (int r = 0; r < N; r++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int c = 0; c < N; c++) {
        int v = Integer.parseInt(st.nextToken());
        if (v == 9) {
          shark = new Shark(r, c);
          ocean[r][c] = 0;
        } else {
          ocean[r][c] = v;
        }
      }
    }
  }
  
  static boolean bfs() {
    boolean[][] visited = new boolean[N][N];
    ArrayDeque<int[]> q = new ArrayDeque<>();
    
    q.add(new int[]{shark.r, shark.c, 0});
    visited[shark.r][shark.c] = true;
    
    int minDist = Integer.MAX_VALUE;
    int targetR = -1, targetC = -1;
    
    while (!q.isEmpty()) {
      int[] cur = q.poll();
      int r = cur[0];
      int c = cur[1];
      int dist = cur[2];
      
      // 업데이트된 최소거리에 도달하면 종료
      if (dist > minDist) break;
      
      for (int d = 0; d < 4; d++) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        
        if (!isInRange(nr, nc)) continue;
        if (visited[nr][nc]) continue;
        if (ocean[nr][nc] > shark.size) continue;
        
        visited[nr][nc] = true;
        int nextDist = dist + 1;
        
        // 먹을 수 있는 사이즈를 발견한다면
        if (ocean[nr][nc] != 0 && ocean[nr][nc] < shark.size) {
          // 가장 가깝거나
          // 거리는 동일하나 우선순위가 높은 물고기에게로 이동
          if (nextDist < minDist ||
              (nextDist == minDist && 
              (nr < targetR || (nr == targetR && nc < targetC)))) {
            minDist = nextDist;
            targetR = nr;
            targetC = nc;
          }
        }
        
        q.add(new int[]{nr, nc, nextDist});
      }
    }
    
    // target이 없으면 더이상 먹을 물고기가 없음을 의미
    if (targetR == -1) return false;
    
    // 아기상어의 이동 업데이트
    answer += minDist;
    shark.r = targetR;
    shark.c = targetC;
    
    // 해당 지점 0으로 초기화 및 eat 증가
    ocean[targetR][targetC] = 0;
    shark.eat++;
    
    // 성장 분기
    if (shark.eat == shark.size) {
      shark.size++;
      shark.eat = 0;
    }
    
    // 다음 이동 준비
    return true;
  }
  
  static boolean isInRange(int r, int c) {
    return 0 <= r && r < N && 0 <= c && c < N;
  }
  
  public static void main(String[] args) throws Exception {
    init();
    while (bfs()) {}
    System.out.print(answer);
  }
}
