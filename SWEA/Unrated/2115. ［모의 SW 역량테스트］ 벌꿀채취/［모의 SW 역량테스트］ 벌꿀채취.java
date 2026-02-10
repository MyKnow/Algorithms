import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int T, N, M, C;
  static int[][] map;
  static int[][] profit;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
    
    map = new int[N][N];
    profit = new int[N][N];
    
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        map[i][j] = Integer.parseInt(st.nextToken());
      }
    }
  }
  
  // 하나의 구간에서 얻을 수 있는 최대 이익
  static int calcProfit(int r, int c) {
    int max = 0;
    
    for (int mask = 1; mask < (1 << M); mask++) {
      int sum = 0;
      int sq = 0;
      
      for (int i = 0; i < M; i++) {
        if ((mask & (1 << i)) != 0) {
          int v = map[r][c + i];
          sum += v;
          sq += v * v;
        }
      }
      
      if (sum <= C) {
        max = Math.max(max, sq);
      }
    }
    return max;
  }
  
  static int solve() {
    // 1단계: 모든 구간의 최대 이익 계산
    for (int i = 0; i < N; i++) {
      for (int j = 0; j <= N - M; j++) {
        profit[i][j] = calcProfit(i, j);
      }
    }
    
    int answer = 0;
    
    // 2단계: 두 구간 선택
    for (int i1 = 0; i1 < N; i1++) {
      for (int j1 = 0; j1 <= N - M; j1++) {
        for (int i2 = i1; i2 < N; i2++) {
          for (int j2 = 0; j2 <= N - M; j2++) {
            
            // 같은 행에서 겹치는 경우 제외
            if (i1 == i2 && j2 < j1 + M && j1 < j2 + M) continue;
            
            int sum = profit[i1][j1] + profit[i2][j2];
            answer = Math.max(answer, sum);
          }
        }
      }
    }
    return answer;
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t <= T; t++) {
      init();
      sb.append("#").append(t).append(" ").append(solve()).append("\n");
    }
    System.out.print(sb.toString());
  }
}