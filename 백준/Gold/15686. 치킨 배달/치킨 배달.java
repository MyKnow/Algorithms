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
  static int N, M;
  static int[][] chickenCoords = new int[13][2];
  static int[][] houseCoords = new int[100][2];
  static int[][] chickenDistances;
  static int chickenSize;
  static int houseSize;
  static int[] selected;
  static int answer;

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    chickenSize = 0;
    houseSize = 0;

    for (int r=0; r<N; r++) {
      st = new StringTokenizer(br.readLine());
      for (int c=0; c<N; c++) {
        int current = Integer.parseInt(st.nextToken());
        if (current == 1) houseCoords[houseSize++] = new int[] { r, c };
        else if (current == 2) chickenCoords[chickenSize++] = new int[] { r, c };
      }
    }

    chickenDistances = new int[houseSize][chickenSize];
    for (int i=0; i<houseSize; i++) {
      for (int j=0; j<chickenSize; j++) {
        chickenDistances[i][j] =
          Math.abs(houseCoords[i][0] - chickenCoords[j][0]) +
          Math.abs(houseCoords[i][1] - chickenCoords[j][1]);
      }
    }

    selected = new int[M];
    answer = Integer.MAX_VALUE;
  }

  static void dfs(int start, int depth) {
    if (depth == M) {
      int sum = 0;

      for (int hIdx=0; hIdx<houseSize; hIdx++) {
        int minDist = Integer.MAX_VALUE;
        for (int i=0; i<M; i++) {
          minDist = Math.min(minDist, chickenDistances[hIdx][selected[i]]);
        }
        sum += minDist;
        if (sum >= answer) return;
      }

      answer = Math.min(answer, sum);
      return;
    }

    for (int i=start; i<chickenSize; i++) {
      selected[depth] = i;
      dfs(i+1, depth+1);
    }
  }

  public static void main(String[] args) throws Exception {
    init();
    dfs(0, 0);
    System.out.print(answer);
  }
}
