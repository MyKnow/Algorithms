import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.Arrays;

// 인덱스 1부터 시작
// M(최소 1)개의 치킨집만을 남기고 모두 폐업
// 도시의 치킨 거리는 모든 집의 치킨 거리의 합
// 도시의 치킨 거리 최솟값 출력

// 완전 탐색
// 길이 M의 치킨집 조합
// 각 조합에서의 "도시의 치킨 거리" 산출
// 그 중 가장 작은 값 반환

// 도시 구역 최대 50*50 = 2500
// 집 최대 개수는 2N(100개, 최소 1개)
// 치킨집의 개수는 M이상 13 이하



public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int N, M;
  static int[][] map;
  static int[][] chickenCoords = new int[13][2];
  static int[][] houseCoords = new int[100][2];
  static int[][] chickenComb;
  static int[][] chickenDistances;
  static int chickenSize;
  static int houseSize;
  static int combinationSize;
  static int combinationIdx;
  static boolean[] isSelected;
  static int answer;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    
    map = new int[N][N];
    chickenSize = 0;
    houseSize = 0;
    for (int r=0; r<N; r++) {
      st = new StringTokenizer(br.readLine());
      for (int c=0; c<N; c++) {
        int current = Integer.parseInt(st.nextToken());
        if (current == 0) continue;
        else if (current == 1) houseCoords[houseSize++] = new int[] { r, c };
        else if (current == 2) chickenCoords[chickenSize++] = new int[] { r, c };
      }
    }
    System.arraycopy(chickenCoords, 0, chickenCoords, 0, chickenSize);
    System.arraycopy(houseCoords, 0, houseCoords, 0, houseSize);
    combinationSize = calcCombination(chickenSize, M);
    chickenComb = new int[combinationSize][M];
    isSelected = new boolean[chickenSize];
    combinationIdx = 0;
    answer = Integer.MAX_VALUE;
  }
  
  static int calcCombination(int n, int r) {
    if (n==r || r == 0) return 1;
    return calcCombination(n-1, r-1) + calcCombination(n-1, r);
  }
  
  static void travelHouse() {
    chickenDistances = new int[houseSize][chickenSize];
    for (int i=0; i<houseSize; i++) {
      int[] hCoords = houseCoords[i];
      int houseR = hCoords[0];
      int houseC = hCoords[1];
      
      for (int j=0; j<chickenSize; j++) {
        int[] cCoords = chickenCoords[j];
        int chickenR = cCoords[0];
        int chickenC = cCoords[1];
        
        chickenDistances[i][j] = Math.abs(chickenR-houseR) +Math.abs(chickenC-houseC);
      }
    }
  }
  
  static void updateCombination(int start, int depth) {
    if (depth == M) {
      int idx = 0;
      for (int i=0; i<chickenSize; i++) {
        if (isSelected[i]) chickenComb[combinationIdx][idx++] = i;
      }
      combinationIdx++;
      return;
    }
    
    for (int i=start; i<chickenSize; i++) {
      isSelected[i] = true;
      updateCombination(i+1, depth+1);
      isSelected[i] = false;
    }
  }
  
  static void updateChickenDistance() {
    for (int[] comb : chickenComb) {
      int sum = 0;

      for (int hIdx = 0; hIdx < houseSize; hIdx++) {
        int minDist = Integer.MAX_VALUE;
        for (int cIdx : comb) {
          minDist = Math.min(minDist, chickenDistances[hIdx][cIdx]);
        }
        sum += minDist;
      }
      answer = Math.min(answer, sum);
  }
}

  
  public static void main(String[] args) throws Exception {
    init();
    travelHouse();
    updateCombination(0, 0);
    updateChickenDistance();
    System.out.print(answer);
  }
}