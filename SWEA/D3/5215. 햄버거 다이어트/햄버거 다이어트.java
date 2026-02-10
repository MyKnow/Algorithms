import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int T;
  static int N, L;
  static int[] score, cal;
  static int maxScore;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    L = Integer.parseInt(st.nextToken());
    
    score = new int[N];
    cal = new int[N];
    
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      score[i] = Integer.parseInt(st.nextToken());
      cal[i] = Integer.parseInt(st.nextToken());
    }
    
    maxScore = 0;
  }
  
  static void dfs(int idx, int scoreSum, int calSum) {
    if (calSum > L) return;
    
    if (idx == N) {
      maxScore = Math.max(maxScore, scoreSum);
      return;
    }
    
    // 현재 재료 선택
    dfs(idx + 1, scoreSum + score[idx], calSum + cal[idx]);
    
    // 현재 재료 미선택
    dfs(idx + 1, scoreSum, calSum);
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t <= T; t++) {
      init();
      dfs(0, 0, 0);
      sb.append("#").append(t).append(" ").append(maxScore).append("\n");
    }
    System.out.print(sb.toString());
  }
}